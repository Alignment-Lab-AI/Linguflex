
# Installation Guide

This guide will help you set up your environment for the project. Please follow the steps carefully.

## Prerequisites
- Python 3.10.9
  https://www.python.org/downloads/release/python-3109/
- NVIDIA CUDA Toolkit installed (11.8 recommended)
  https://developer.nvidia.com/cuda-11-8-0-download-archive
- NVIDIA cuDNN installed (8.7.0 for CUDA 11.x recommended):
  https://developer.nvidia.com/rdp/cudnn-archive
- ffmpeg installed
  https://ffmpeg.org/download.html

## Step-by-Step Installation

1. **Set up Python Virtual Environment:**
   ```bash
   python -m venv test_env
   test_env\Scripts\activate.bat
   ```

   If you have multiple Python installations or environments, use path_to_your_python_exe/python.exe -m venv test_env, where path_to_your_python_exe is the specific path to the Python 3.10.9 executable needed for this project.

2. **Upgrade pip:**
   ```bash
   python -m pip install --upgrade pip
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install RealtimeSTT
   pip install RealtimeTTS
   pip install torch==2.2.0+cu118 torchaudio==2.2.0+cu118 --index-url https://download.pytorch.org/whl/cu118
   pip install numpy==1.23.5
   pip install pyautogui
   pip install opencv-python
   ```

   **Note:** Adjust Torch installation according to your CUDA version.

4. **Deepspeed Installation:**
   ```bash
   pip install deepspeed
   ```

   If pip install of deepspeed does not work (can be complicated on Windows), you can try to install a deepspeed python wheel for your system from here:
   - [Deepspeed on Windows](https://github.com/daswer123/deepspeed-windows-wheels)
   - [Alltalk TTS Deepspeed Options](https://github.com/erew123/alltalk_tts?tab=readme-ov-file#-deepspeed-installation-options)

5. **Install llama-cpp-python:**
   ```bash
   pip install llama-cpp-python --force-reinstall --upgrade --no-cache-dir --verbose
   ```

   **Note:** If pip install of llama-cpp-python fails you may need to set some environment variables and copy files based on your CUDA version:
   - Set environment variables:
     ```bash
     set CMAKE_ARGS=-DLLAMA_CUBLAS=on
     set FORCE_CMAKE=1
     ```
   - Also it may be needed to copy all four MSBuildExtensions files based on your CUDA version (11.8 or 12.3) from:
     ```
     C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\extras\visual_studio_integration\MSBuildExtensions   
     ```
     to
     ```
     C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\MSBuild\Microsoft\VC\v170\BuildCustomizations
     ```
     before executing the pip install command.

6. **Download models:**
   ```bash
   python download_models.py
   ```

7. **Adjust settings:**
   - adjust lingu/settings.yaml to configure linguflex to your environment
   - setup the needed environment keys
     - OPENAI_API_KEY to use GPT API for answers
     - AZURE_SPEECH_KEY, AZURE_SPEECH_REGION to use Azure TTS
     - ELEVENLABS_API_KEY to use Elevenlabs TTS
     - GOOGLE_API_KEY to use Music Playout

8. **Start linguflex:**
   - start run.bat or type:
      ```bash
      python -m lingu.core.run
      ``` 