# Geometric Properties of Sets in Minkowski Spaces

This is an interactive **Streamlit** app for exploring and computing various geometric properties of point sets in spaces with the **Minkowski metric**.

---

##  Features

The application allows users to:

-  **Compute the diameter** of a point set (max distance between all pairs)
-  **Compute the distance between two sets** of points
-  **Visualize Minkowski balls** (closed, open, and sphere-like) in 2D for any `p`-metric

---

## Technologies Used

- Python 3.x
- [Streamlit](https://streamlit.io/)
- NumPy
- Matplotlib

---

## Project Structure

| File            | Description |
|------------------|-------------|
| `app.py`         | Main navigation and page setup |
| `ball_d2.py`     | 2D visualization of Minkowski balls |
| `set_diam.py`    | Diameter calculation of a point set with distance matrix |
| `set_dist.py`    | Distance calculation between two point sets |
| `func.py`        | Utility functions (Minkowski metric, plots, LaTeX output) |

---

## App Pages

- **Diameter of a Set**
- **Distance Between Sets**
- **Minkowski Ball in 2D**
- **LaTeX Export of Distance Matrix**

---

##  How to Run

1. Install the required libraries:

```bash
pip install streamlit numpy matplotlib
```
2. Run the app:
```
streamlit run app.py
```
3. The app will open automatically in your browser.

You can also run app without installing anything, using URL [Streamlit Page for Apps](https://kursapp-pg9qzqkjjdkuyezpwiurdn.streamlit.app/)

## App Overview

- Interactive point input forms
- Visual representation of balls for various Minkowski norms
- Support for `p` in (0, ∞) and ∞ (Chebyshev distance)
- Dynamic LaTeX output for distance matrices
