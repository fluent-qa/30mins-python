# Jupyter Notes to Web


## installation


```shell
pdm add voici
voici notebooks/
voici build --contents my-notebook.ipynb
cd _output
python -m http.server

jupyter lite build
```
