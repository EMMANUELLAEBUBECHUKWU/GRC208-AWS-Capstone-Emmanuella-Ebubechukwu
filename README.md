# GRC208 AWS Integrated GRC Platform
## Capstone Project — Emmanuella Ebubechukwu

**Student:** Emmanuella Ebubechukwu  
**Student ID:** 2025/GRC/10041  
**Programme:** GRC Engineering (CGRCE)  
**Institution:** International Cybersecurity and Digital Forensics Academy (ICDFA)  
**Course:** GRC208 — Governance, Risk, and Compliance Capstone  
**Submission Date:** March 29, 2026  

---

## Overview

This repository contains the complete deployment of an AWS-native Governance, Risk, and Compliance (GRC) platform, built and submitted as the GRC208 capstone project. The platform was deployed from scratch in the AWS Academy Learner Lab environment using AWS CloudShell, Infrastructure as Code via CloudFormation, and a serverless Lambda-based compliance automation engine.

The project demonstrates how modern organisations can move beyond manual, spreadsheet-based compliance tracking and build a continuously monitored, automatically alerting GRC platform using AWS native services.

---

## Deployment Environment

| Detail | Value |
|--------|-------|
| AWS Account | 975049998247 |
| Region | us-east-1 |
| Deployment Method | AWS CloudShell via AWS Academy Learner Lab |
| Network | VPC vpc-013f73c5f62dd802b (10.0.0.0/16) |
| Database Endpoint | grc-capstone-db.cnok20k42m82.us-east-1.rds.amazonaws.com |
| Lambda Function | grc-compliance-monitor (Python 3.11, 256 MB) |
| CloudTrail Trail | grc-trail (IsLogging: True) |
| Test Results | 22/22 passing |

---

## Architecture Summary

The platform is built on a multi-tier VPC architecture with public and private subnets across two availability zones. All application compute and database resources are placed in private subnets with no direct internet exposure.

**Network Layer**
- VPC (10.0.0.0/16) with two public and two private subnets
- NAT Gateway for outbound-only private subnet internet access
- Application Load Balancer in public subnets
- Four security groups with scoped least-privilege rules

**Data Layer**
- Amazon RDS MySQL 8.0 (grc-capstone-db, db.t3.micro) — GRC relational data
- Amazon S3 — evidence storage and compliance reports
- Amazon DynamoDB — three tables for real-time compliance status
- AWS KMS — encryption at rest for RDS and S3

**Application Layer**
- AWS Lambda (grc-compliance-monitor) — hourly compliance automation
- Amazon ECS Fargate — containerised GRC dashboard application
- AWS EventBridge — hourly schedule triggering compliance Lambda

**Security & Compliance Layer**
- AWS Config — configured for 596 resource types, continuous recording
- AWS CloudTrail — grc-trail, all API calls logged to S3
- Amazon CloudWatch — alarm grc-high-non-compliance (<80% threshold)
- Amazon SNS — compliance threshold alert notifications

---

## Compliance Frameworks Supported

The platform supports mapping controls to the following six frameworks:

| Framework | Focus Area |
|-----------|------------|
| ISO 27001:2022 | Information Security Management System |
| NIST Cybersecurity Framework | Risk management and security controls |
| PCI DSS 3.2.1 | Payment card data protection |
| HIPAA | Health information privacy and security |
| GDPR | EU personal data protection |
| SOC 2 | Service organisation control assurance |

---

## Repository Structure
