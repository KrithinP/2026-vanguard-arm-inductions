# 📸 Task 3 — Panorama or Bust (The Wider Picture)

> **Priority: 3 of 3.** Pure Python. This one mirrors a real Mars Rover challenge deliverable — do it well and you're already contributing.

## The problem
In the field, documentation is everything. A single narrow photo of a worksite is useless to the analysis team — we need wide, accurate **1:3 panoramas** with scale and direction baked in. The catch: the camera only takes small overlapping snapshots, and naive copy-paste leaves ugly seams and distorted geometry.

## Your mission
Build a custom **image-stitching pipeline** — essentially coding your phone's "Panorama Mode" from scratch with classical computer vision. Detect overlapping features across a set of photos, mathematically align them, and blend them into a clean, annotated wide-angle shot.

## What you need to do

1. **Gather intel.** Shoot **5–8 overlapping images** per site (aim for ~30–40% overlap between neighbours). Do this for **2–3 different sites**.
2. **Find the commonalities.** Use a feature detector — **SIFT or ORB** — to find matching points between images. **Justify your choice** (speed vs robustness vs licensing).
3. **Align & stitch.** Use **RANSAC + homography estimation** to reject bad matches and warp the images into one frame. (You may lean on OpenCV primitives like `findHomography` and `warpPerspective` — the interesting work is the pipeline, matching, and blending.)
4. **Polish & annotate.** Blend the seams so they disappear. Crop to a strict **1:3 (height:width)** ratio, and overlay a **scale bar** and a **cardinal direction arrow (N/E/S/W)**.

## Deliverables
1. Your complete Python pipeline in `src/task3/`.
2. **2–3 finished panoramas** meeting the 1:3 ratio and annotation requirements.
3. A short, **honest report**: where did stitching fail (repetitive textures? low overlap? moving objects? exposure changes?), and how did you fix or work around it? This report is a big part of the score — we learn the most from your failures.

## ⭐ Optional shared benchmark
Drop your pipeline over the images in `assets/task3/benchmark/` (a fixed set we provide) in addition to your own photos. This lets us compare approaches head-to-head — and the strongest pipelines here directly inform how we tackle the panorama task at competition. If your approach is good, we want to build on it (with credit).

## Hints
- **ORB** is fast and license-free; **SIFT** is more robust to scale/rotation but slower. Try both and *report the difference* — that comparison is worth marks.
- Ratio-test your matches (Lowe's ratio) before RANSAC — garbage matches in, garbage homography out.
- Shoot by **rotating in place**, not walking sideways — pure rotation is what homography assumes. This single tip fixes most "it won't stitch" problems.
- For blending, even simple feathering across the overlap beats a hard seam.
