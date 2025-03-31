# Base image with Python and CUDA (compatible with LightGBM + NVIDIA drivers)
FROM nvidia/cuda:12.3.2-devel-ubuntu22.04

# Set non-interactive mode for apt
ENV DEBIAN_FRONTEND=noninteractive

# Install OS dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-dev python3-venv \
    build-essential cmake git wget unzip \
    libboost-dev libboost-system-dev libboost-filesystem-dev \
    libssl-dev curl vim && \
    rm -rf /var/lib/apt/lists/*

# Create working directory
WORKDIR /app

# Copy your repo (update to actual path if needed)
COPY . .

# Install Python dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Install Ember in editable mode (assumes ember/ is inside the repo)
RUN pip3 install -e ./ember

# Build LightGBM from source with GPU support
RUN git clone --recursive https://github.com/microsoft/LightGBM && \
    cd LightGBM && mkdir build && cd build && \
    cmake -DUSE_GPU=1 .. && make -j$(nproc) && \
    cd ../python-package && python3 setup.py install

# Default command (override when running container)
CMD [ "python3" ]
