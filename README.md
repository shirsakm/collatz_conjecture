# Collatz Conjecture Graph Plotter

This prgoram graphs the steps taken by any number when repeatedly subjected to a function under the bounds of the Collatz conjecture. It then prints the number of steps taken in the command-line interface.

## Background

Collatz conjectured that any number when repeatedly applied to the function

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/9b2a03faf9d31a8de0abb3c4a3d318490105da12)

always yields the value of unity.

Some example graphs are shown below,

![The steps graph of 27](https://github.com/shirsakm/collatz_conjecture/blob/master/showcase/27.png)

![The steps graph of 5, 7, 13 plotted simultaneously](https://github.com/shirsakm/collatz_conjecture/blob/master/showcase/5_7_13.png)

## Usage

### Linux or MacOS

1. (Optional) Make and activate a virtual environment

```sh
$ python -m venv .venv
```

```sh
$ source .venv/bin/activate
```

2. Install the `matplotlib`

```sh
$ pip install -r requirements.txt
```

3. Run by calling `main.py`

```sh
$ python main.py numbers
```

### Windows

1. (Optional) Make and activate a virtual environment

```sh
$ python -m venv .venv
```

```sh
$ .venv\bin\activate
```

2. Install the `matplotlib`

```sh
$ pip install -r requirements.txt
```

3. Run by calling `main.py`

```sh
$ python main.py numbers
```
