# Secure Code Review for Alturo Manual

This document outlines the findings from a secure code review of the **Alturo Manual** website. We focus on identifying vulnerabilities related to SQL Injection and Cross-Site Scripting (XSS), providing remediation strategies to enhance the application's security posture.

## 1. SQL Injection Vulnerability Analysis

### __Vulnerability Overview__
SQL Injection (SQLi) vulnerabilities arise when user input is directly included in SQL queries without proper sanitization. Attackers can exploit this weakness to manipulate database queries, allowing actions such as bypassing authentication.

### __Example SQL Query__
```sql
SELECT * FROM users WHERE username = 'admin' AND password = 'user_input';
