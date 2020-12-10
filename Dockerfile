FROM guillaumeai/tf

WORKDIR /work
COPY gixrequirements.txt .
RUN pip install -r gixrequirements.txt

WORKDIR /model

COPY . .

RUN echo "See /model and https://github.com/GuillaumeIsabelleX/gix-textgenrnn#examples"


