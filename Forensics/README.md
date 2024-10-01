# Forensics Tasks: Dam Location Identification and ZIP File Password Cracking

## 📖 Overview

This repository contains forensic tasks aimed at identifying the location of a dam and cracking the password of a ZIP file. The tasks were completed using Python scripts and various libraries to enhance investigative skills and demonstrate practical applications in cybersecurity.

---

## 🔍 Tasks Completed

### 1. **Dam Location Identification**

- **Objective:** Identify the location of a specific dam using geographical coordinates.
- **Methodology:** 
  - Utilized latitude and longitude values obtained through decoding processes (e.g., Base64 decoding).
  - Mapped the coordinates using Google Maps to pinpoint the location.
- **Coordinates Used:** 
  - Latitude: `10.854753988372662`
  - Longitude: `76.66236870807573`
- **Location Identified:** Malampuzha Dam

### 2. **ZIP File Password Cracking**

- **Objective:** Develop a Python script to crack the password of a ZIP file.
- **Tools Used:** 
  - `zipfile` module (part of Python's standard library)
  - `itertools` module for generating potential passwords
- **Methodology:**
  - Created a script that iterates through a wordlist to attempt password combinations.
  - Implemented error handling to identify successful password entries.
- **Script:** 
  - Refer to the `zip_cracker.py` file in this repository.

---
