from .events import events
from .state import State
import threading


class Logic:
    """
    Base class for implementing logic with event handling capabilities.
    """

    def __init__(self):
        """Initializes the LogicBase with default attributes."""
        self.server_ready_event = threading.Event()
        self.set_ready = False
        self.ready_event = threading.Event()
        self.state: State = None
        self.inference_manager = None
        self.server = None
        self.module_name = "Unknown"
        self.abort = False

    def inference(
            self,
            inference_object,
            prompt,
            content,
            model="gpt-3.5-turbo-1106"):
        """
        Inference logic.

        Args:
            inference_object: The inference object to use.
            prompt: The prompt to use for inference.
            content: The content to analyze or process.
            model: The model to use for inference.
        """
        return self.inference_manager.inference(
            inference_object,
            prompt,
            content,
            model)

    def llm(self, **kwargs):
        return self.inference_manager.llm(**kwargs)

    def ready(self):
        """Sets the ready event."""
        self.ready_event.set()

    def add_listener(
            self,
            event_name: str,
            trigger_module_name: str,
            callback
    ):
        """Registers a callback for a specified event.

        Args:
            event_name (str): The name of the event to listen for.
            trigger_module_name (str): The name of the module triggering
              the event.
            callback: The function to call when the event is triggered.
        """
        events.add_listener(event_name, trigger_module_name, callback)

    def trigger(self, event_name: str, data=None):
        """Triggers an event with optional data.

        Args:
            event_name (str): The name of the event to trigger.
            data: Optional data to pass with the event.

        Returns:
            The result of the event trigger.
        """
        return events.trigger(event_name, self.module_name, data)

    def trigger_with_params(self, event_name: str, **kwargs):
        """Triggers an event with named parameters.

        Args:
            event_name (str): The name of the event to trigger.
            **kwargs: Arbitrary keyword arguments to pass with the event.

        Returns:
            The result of the event trigger.
        """
        return events.trigger_with_params(
            event_name,
            self.module_name,
            **kwargs
        )

    def init(self):
        """
        Placeholder for initialization logic.
        Can be overridden by subclasses.
        """
        if not self.set_ready:
            self.ready()

    def init_finished(self):
        """
        Placeholder for initialization finished logic.
        Can be overridden by subclasses.
        """
        pass

    def post_init_processing(self):
        """
        Placeholder for post initialization processing logic.
        Can be overridden by subclasses.
        """
        pass

    def process_response_stream(self, stream):
        """
        Answer processing logic.
        Consumes the assistant response stream, triggers events,
        and returns the assistant text.
        """
        assistant_text = ""

        if not self.abort:
            for chunk in stream:
                if not chunk or len(chunk) == 0:
                    # happens sometimes
                    continue

                if self.abort:
                    break
                if not assistant_text:
                    self.trigger("assistant_text_start")

                assistant_text += chunk
                self.trigger("assistant_text", assistant_text)
                self.trigger("assistant_chunk", chunk)

        return assistant_text
