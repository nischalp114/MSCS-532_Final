# HPC Data Structure Optimization Project

This repository contains the implementation portion of the project for:

**MSCS-532-B01 — Algorithms and Data Structures (Fall 2025)**  
**Topic:** Optimization in High-Performance Computing (HPC)  
**Student:** Nischal Pokharel  

---

## 📌 Project Overview

This project demonstrates a key optimization technique identified in the empirical research study  
*“An Empirical Study of High Performance Computing (HPC) Performance Bugs”* — specifically:

### ✅ **Data Structure Optimization for Data Locality**

High-performance applications often suffer from inefficient memory access patterns, especially when using pointer-based structures like linked lists. Replacing such structures with contiguous memory layouts (arrays, vectors, NumPy arrays) improves cache locality and performance.

This project provides a small benchmark comparing:

- A **custom singly linked list**
- A **Python list** (dynamic array)
- A **NumPy array** (contiguous typed array)

---


