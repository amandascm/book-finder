**OBS.:** O README.md foi editado além do prazo para acréscimo do link do vídeo II com correção do volume do áudio. Os dois vídeos estão presentes na descrição do projeto abaixo, mas recomendamos fortemente que assista a versão com áudio melhorado, com mesmo conteúdo da versão anterior - **nenhum outro arquivo foi editado além do prazo (vide histórico de commits).**
# book-finder
Search engine and information retrieval tool for books

## Group
* [Amanda Soares de Castro Moraes](https://github.com/amandascm/)
* [Luís Eduardo Martins Alves](https://github.com/Luis-Alves2)
* [Tales Tomaz Alves](https://github.com/tta13)

## Milestones

- [Crawler](/crawler/)
- [Classifier](/classifier/)
- [Wrapper](/wrapper/)
- [Crawled data](/data/crawled/)
- [Extracted data](/data/wrapped/)
- [Slides I](https://docs.google.com/presentation/d/1oatbT9H2xB26mJvtc81HOb7a5bKktGGPeio9vy2M3P4/view?usp=sharing)
- [Video I](https://drive.google.com/file/d/1jE_3_5hpdxuBUR-ympyQzNhP1HXir0Gf/view?usp=sharing)
- [Inverted Index](/data/inverted-index/)
- [Query module code](/search_engine/query/)
- [Query response composition app](/search_engine/gui/)
- [Slides II](https://docs.google.com/presentation/d/1A99vLJuXnCeUq5nR6NCyVuH1trXh5y6sXhDMa_yERb4/view?usp=sharing)
- [Video II FIXED AUDIO - watch this one](https://drive.google.com/file/d/1tAEswHlbnFcuFJa7mT6ZLr29EyPGNAXy/view?usp=sharing)
- [Video II](https://drive.google.com/file/d/1IToKj-I96QeYh540efF8VbCKljhEr6Jf/view?usp=sharing)

## Search Engine App Demo
[Access the demo video here](https://drive.google.com/file/d/1suDBYO7FVyiUUWIsCCLwyDGWQw0P3tLl/view?usp=sharing).


## Dev environment and code execution

Commands to run the search engine app:

### Using Docker

Build image:

```bash
docker build -t book-finder .
```

Start container:

```bash
docker run -p <port>:<port> -e PORT=<port> book-finder # e.g. port = 5000
```

Access `localhost:<port>` in your web browser.

### Using Python Environment

```bash
# Create Python venv
python -m venv .venv

# Activate venv
# Windows
.venv\Scripts\activate
# Linux
source .venv/bin/activate

# Install dependencies and local package
pip install -r requirements

pip install -e .
```

To run the Book Finder app and test it locally with your own queries do:

```bash
cd search_engine
cd gui
flask run
```

If you wish to run the app on debug mode, run the command below instead of `flask run`:

```
python index.py
```
