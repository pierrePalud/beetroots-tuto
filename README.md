# beetroots-tuto

## Step 0 : install

Install Docker Desktop (choose the version adapted to your OS): <https://www.docker.com/get-started/>

Then open a terminal wherever you want to install this tutorial, and run

```shell
git clone https://github.com/pierrePalud/beetroots-tuto.git
cd beetroots-tuto
docker build -t beetroots-tuto .
```

Then open vscode, click on the green button (at the extreme bottom left corner), and select "Reopen in container".

## Step 1 : nnbma

play with the notebooks/01 notebook.

## step 2 : beetroots

Once the mode is trained and saved, to run beetroots, simply run:

```shell
python beetroots_tuto/synthetic_case_nn.py input.yaml ./data/synthetic_case ./data/models .
```

To change some parameters of the reconstruction, modify the `data/synthetic_case/input.yaml` file.
