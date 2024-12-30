{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPdPKBdHZVv7bTnwUDeW2o5",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/harikiranirla/harikiranirla/blob/main/Agent_problem.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "T2WaRZmbwnkA"
      },
      "outputs": [],
      "source": [
        "def agent_program(percept):\n",
        "    \"\"\"\n",
        "    Agent function for the vacuum cleaner agent.\n",
        "\n",
        "    Args:\n",
        "        percept: The state of the current cell (0 for Clean, 1 for Dirty).\n",
        "\n",
        "    Returns:\n",
        "        The action to be taken ('Suck' or 'Move').\n",
        "    \"\"\"\n",
        "\n",
        "    # Table-driven agent\n",
        "    action_table = {\n",
        "        0: 'Move',  # Clean: Move to another square\n",
        "        1: 'Suck'   # Dirty: Clean the current square\n",
        "    }\n",
        "\n",
        "    # Lookup the action in the table\n",
        "    action = action_table[percept]\n",
        "\n",
        "    return action\n",
        "\n"
      ]
    }
  ]
}