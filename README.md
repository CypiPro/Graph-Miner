# Graph Miner

## Problem Description

In many cases, numerical data is available only in the form of graphs, for example, in
scientific publications, reports, manuals, or presentations. Often, access to the original
data files is not possible, and manually extracting points from a graph is
time-consuming, imprecise, and prone to human error.

Therefore, a tool that can automatically or semi-automatically read data from any type
of graph, process it, and save it in a format suitable for further analysis is needed.

Project Objective

The goal of the project is to develop a program that enables:
* fast and accurate extraction of numerical values from graphs stored as images or
PDF files,

* automatic or semi-automatic curve extraction,

* saving results in a data-table format (CSV or Excel),

* support for various types of plots and multiple data series,

* visual validation of the extraction accuracy through an overlay control image.

The program should be a tool that saves time, eliminates manual transcription errors,
and allows processing of graphs even when the original digital data is unavailable.

## Program Workflow

### Manual Mode

The user manually selects a few reference points on the graph-such as the start and
end of the X-axis and the Y-axis. Based on these anchor points, the program converts
pixel positions into actual graph values. It then detects the curve in the image and
exports its numerical representation to a CSV file.

### Automatic Mode

The program automatically detects:

* the axes of the chart,

* axis tick marks,

* numerical labels defining the scale,

* curves shown in the plot.

## Additional Features

1. Support for plots with multiple lines:
The program must separate individual curves and generate data for each series
independently.

2. Export options:
Results can be saved in CSV or Excel format.

3. Control image generation:
The program generates a verification image in which the extracted points are
overlaid on the original graph, enabling easy visual inspection of accuracy.