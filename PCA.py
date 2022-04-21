{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "PCA.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyOiPGdOhQZj9ePoIDhRHv4n",
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
        "<a href=\"https://colab.research.google.com/github/GokulAnanthM/GokulAnanthM/blob/main/PCA.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np"
      ],
      "metadata": {
        "id": "OVKbdEKsREqf"
      },
      "execution_count": 20,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "x = np.random.randint(50,90,100).reshape(20,5)\n",
        "print(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YEwiUOrLbdkx",
        "outputId": "9d86b1be-adc2-4bf9-9dd2-c0ed5b8227e6"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[70 65 73 89 50]\n",
            " [74 81 89 84 88]\n",
            " [62 68 76 72 60]\n",
            " [76 65 61 53 66]\n",
            " [86 61 51 63 82]\n",
            " [75 51 74 88 70]\n",
            " [53 57 71 54 75]\n",
            " [79 81 77 68 73]\n",
            " [65 89 89 50 80]\n",
            " [74 77 61 59 75]\n",
            " [81 52 84 74 56]\n",
            " [73 52 62 56 65]\n",
            " [70 66 85 52 50]\n",
            " [74 55 69 71 65]\n",
            " [84 72 74 62 86]\n",
            " [68 87 88 78 76]\n",
            " [56 61 83 72 72]\n",
            " [87 64 66 87 65]\n",
            " [63 81 86 63 55]\n",
            " [64 74 58 66 54]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        " xmean=x-np.mean(x,axis=0)\n",
        " xmean"
      ],
      "metadata": {
        "id": "hoxNZTLJRqi_",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "5e0177db-d068-4141-85ab-df2e856f91be"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[  6.1 ,  -3.15,  -3.9 ,  -3.75,  18.  ],\n",
              "       [ -0.9 , -21.15,  -4.9 , -14.75,   8.  ],\n",
              "       [  9.1 ,   2.85,  11.1 ,   1.25,  -9.  ],\n",
              "       [ 16.1 ,   2.85,   2.1 , -10.75,  -3.  ],\n",
              "       [ 14.1 ,  16.85,   7.1 , -13.75,   3.  ],\n",
              "       [-19.9 ,  -3.15,   2.1 ,  19.25,  14.  ],\n",
              "       [ 11.1 ,  13.85,   6.1 ,  10.25,  10.  ],\n",
              "       [-13.9 , -16.15,   8.1 ,  -4.75,  -9.  ],\n",
              "       [ 11.1 ,  16.85, -13.9 ,  21.25, -12.  ],\n",
              "       [-18.9 ,  15.85,  12.1 ,  -5.75,  -1.  ],\n",
              "       [ -1.9 ,   3.85,  -0.9 ,  -4.75,   6.  ],\n",
              "       [ 18.1 , -11.15,   1.1 ,   3.25,  -9.  ],\n",
              "       [-11.9 ,  -4.15, -14.9 ,   6.25, -10.  ],\n",
              "       [-13.9 ,  10.85,  -9.9 ,  -8.75,   9.  ],\n",
              "       [  8.1 ,  -0.15,  -7.9 ,  20.25,   8.  ],\n",
              "       [ 10.1 ,  -0.15, -16.9 , -16.75,   9.  ],\n",
              "       [-11.9 ,  -4.15,  12.1 ,  19.25, -20.  ],\n",
              "       [ -5.9 , -18.15, -12.9 , -17.75,   0.  ],\n",
              "       [ 14.1 ,  15.85,  10.1 , -14.75,  -3.  ],\n",
              "       [-18.9 , -18.15,  14.1 ,  15.25,  -9.  ]])"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "covar=np.cov(xmean, rowvar=False)\n",
        "covar"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9Ts63pUhfRcS",
        "outputId": "92041751-3e71-4e1e-d8b0-0101715210c8"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[175.67368421,  55.12105263, -18.11578947, -38.65789474,\n",
              "         10.47368421],\n",
              "       [ 55.12105263, 155.60789474,  10.96315789,   2.40789474,\n",
              "         14.26315789],\n",
              "       [-18.11578947,  10.96315789, 102.51578947,  17.5       ,\n",
              "        -31.15789474],\n",
              "       [-38.65789474,   2.40789474,  17.5       , 183.98684211,\n",
              "        -37.15789474],\n",
              "       [ 10.47368421,  14.26315789, -31.15789474, -37.15789474,\n",
              "        102.21052632]])"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "eigen_values , eigen_vectors = np.linalg.eigh(covar)\n",
        "eigen_values"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jXt9gVhVfRem",
        "outputId": "d59559c8-3846-4818-c63a-80ce100852bd"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([ 60.17481403, 110.1539934 , 113.67183339, 185.77313366,\n",
              "       250.22096236])"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "eigen_vectors"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jV1dtMZuhMdE",
        "outputId": "b93f681d-a1cf-437c-fd1f-582b489fe8df"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[-0.25204124, -0.62673279,  0.06898458,  0.32500122, -0.65825265],\n",
              "       [ 0.31823319,  0.59430492, -0.08029639,  0.62300936, -0.38851142],\n",
              "       [-0.59590179,  0.09328654, -0.74434201,  0.22787915,  0.17385266],\n",
              "       [-0.19977511, -0.12898105,  0.47019691,  0.63674757,  0.56295755],\n",
              "       [-0.66347103,  0.47819366,  0.46223745, -0.22103658, -0.26194727]])"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sorted_index = np.argsort(eigen_values)[::-1]\n",
        "sorted_index"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UDspBcoahPua",
        "outputId": "8249fd6c-9d85-4c29-886c-0176512ee12a"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([4, 3, 2, 1, 0])"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sorted_eigenvectors = eigen_vectors[:,sorted_index]\n",
        "sorted_eigenvectors"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RsTZ1SPqhQJo",
        "outputId": "0fe04114-5c2b-4806-a0b6-0be57716b36d"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[-0.65825265,  0.32500122,  0.06898458, -0.62673279, -0.25204124],\n",
              "       [-0.38851142,  0.62300936, -0.08029639,  0.59430492,  0.31823319],\n",
              "       [ 0.17385266,  0.22787915, -0.74434201,  0.09328654, -0.59590179],\n",
              "       [ 0.56295755,  0.63674757,  0.47019691, -0.12898105, -0.19977511],\n",
              "       [-0.26194727, -0.22103658,  0.46223745,  0.47819366, -0.66347103]])"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sorted_eigenvalue = eigen_values[sorted_index]\n",
        "sorted_eigenvalue"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-86YYd1JhQSY",
        "outputId": "475cdc5d-2a40-4cff-d6a3-6d0843e815a2"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([250.22096236, 185.77313366, 113.67183339, 110.1539934 ,\n",
              "        60.17481403])"
            ]
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "n = 2 \n",
        "eigenvector_subset = sorted_eigenvectors[:, 0:n]\n",
        "eigenvector_subset"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "J-FUGsz3hQqS",
        "outputId": "b75d5c82-69cf-4761-ffaf-2976a9491be9"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[-0.65825265,  0.32500122],\n",
              "       [-0.38851142,  0.62300936],\n",
              "       [ 0.17385266,  0.22787915],\n",
              "       [ 0.56295755,  0.63674757],\n",
              "       [-0.26194727, -0.22103658]])"
            ]
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "X_reduced = np.dot(eigenvector_subset.transpose(),xmean.transpose()).transpose()\n",
        "X_reduced"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "K-23T4MGifJl",
        "outputId": "e477d60c-89e2-4764-fa92-e82bc659ad42"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[-10.29569729,  -7.23516245],\n",
              "       [ -2.44163602, -25.74607616],\n",
              "       [ -2.10636977,  10.04781005],\n",
              "       [-16.60598646,   1.30471601],\n",
              "       [-23.11993409,   7.27977824],\n",
              "       [ 21.85780025,   1.21142095],\n",
              "       [ -8.47614432,  17.94255289],\n",
              "       [ 16.51585501, -13.76851885],\n",
              "       [ -1.16335873,  27.12102582],\n",
              "       [  5.41162757,   3.04925106],\n",
              "       [ -4.64728833,  -2.77477791],\n",
              "       [ -3.20409518,   3.24539361],\n",
              "       [ 12.99308175,  -3.65836475],\n",
              "       [ -4.07018243,  -7.57473943],\n",
              "       [  2.65730636,  11.86465882],\n",
              "       [-21.31524937, -13.31694762],\n",
              "       [ 27.62502438,  12.98245647],\n",
              "       [ -1.30002276, -27.46703751],\n",
              "       [-21.20113859,   8.02987823],\n",
              "       [ 32.886408  ,  -2.53731747]])"
            ]
          },
          "metadata": {},
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "OyVu0hVVkscD"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}