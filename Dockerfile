FROM pytorch/pytorch
COPY . /src
WORKDIR /src
RUN python -m pip install --upgrade pip wheel setuptools
RUN python -m pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"] 
