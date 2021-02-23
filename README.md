<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Project Title</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Few lines describing your project.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

In this homework, we write a program to simulate the Schelling  Model. 

The Following are some basic rules that this program built with:

1. The world is a 50 $\times$ 50 grid, for a total of G = 2500 cells.
2. The agents are always 50% X and 50% O. In the visualization program, blue grid represent X and red grid represent O. In the case that world contains agent with different satisfaction threshold, the deeper color grid represent the higher threshold one.
3. The Satisfaction Threshold is measured by the number of same type agents in neighbor of 8.
4. If an agent is unsatisfied, it will try to find a empty space that make him happy, using 8-distance to find the closest cell. It will move to the empty space if it can find one, if not, it will stay at its place this iteration.
5. The agent will be allowed to go back to its previous place.
6. When agent is checking if an empty space is satisfied, if neighbor of 8 of the empty space contains the agent itself, it does not count as a similar agent.
7. Agents are updated according to the cell they occupy, left-to-right, top-to-bottom. Start at the top-left corner in the grid, move left-to-right along the first row, and update all the agents you encounter. Once done with the row, move down to the leftmost cell of the second row, and repeat the above steps.
8. All the agent move at the same time in one iteration.

## 🏁 Getting Started <a name = "getting_started"></a>

Download the code into the local machine and go into the directory contains Schelling_Model.py using terminal

### Prerequisites

This program requires numpy

```
pip install numpy
```

This program requires matplotlib

```
pip install matplotlib
```

This program requires Stremlit

```
pip install streamlit
```
## 🎈 Usage <a name="usage"></a>

Run the python file with Streamlit under the code directory

```
Streamlit run Schelling_Model.py
```

## ⛏️ Built Using <a name = "built_using"></a>

- [Streamlit](https://www.streamlit.io/) - Frontend
- [Python 3.7.9 64bit] - Backend

## ✍️ Authors <a name = "authors"></a>

- [@Zhanhong Huang](https://github.com/Seekerzero)

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- This program's basic data structure and front-end distribution was inspired by Adil Moujahid and his blog: [http://adilmoujahid.com/posts/2020/05/streamlit-python-schelling/](http://adilmoujahid.com/posts/2020/05/streamlit-python-schelling/).
- [@adilmoujahid](https://github.com/adilmoujahid)
