# beetroots-tuto

## Step 0 : install

```shell
git clone https://github.com/pierrePalud/beetroots-tuto.git
cd beetroots-tuto
docker build -t beetroots-tuto .
```

Then open vscode, click on vscode bottom left corner, and select "Reopen in container"

## Step 1 : nnbma

play with the notebooks/01 notebook.

## step 2 : beetroots

```shell
poetry shell

python beetroots_tuto/synthetic_case_nn.py input.yaml ./data/synthetic_case ./data/models .
```
