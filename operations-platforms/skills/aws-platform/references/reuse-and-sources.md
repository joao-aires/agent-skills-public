# AWS reuse and sources

Source decisions for the `aws-platform` method. This skill is original guidance informed by reviewed public material; no upstream instructions, command policies, provider versions or pricing claims are imported. Links are provenance and optional references, not runtime dependencies or authorization.

Checked 2026-11-16. Repository pages and licenses were inspected; no upstream skill was behaviorally evaluated, and no AWS account or console was used.

## Reuse matrix

| Source | What is useful to reuse | What is not adopted | License and disposition |
| --- | --- | --- | --- |
| [github/awesome-copilot: `aws-cloud-development`](https://github.com/github/awesome-copilot/tree/main/plugins/aws-cloud-development) | Decomposition into cost, health, resource query and Well-Architected review concerns; read-only resource-query boundary; review questions that connect IaC to architecture | Slash commands, agent personas, GitHub issue creation, action-oriented workflows, provider/version assumptions. No raw acquisition: the plugin contains action-heavy commands and agents that would duplicate collection authority. | MIT. Reference only. |
| [wshobson/agents: `cloud-infrastructure`](https://github.com/wshobson/agents/tree/main/plugins/cloud-infrastructure) | Terraform module-library structure, module composition patterns, cloud infrastructure skill separation | Provider pins, module implementations, example resources, cost and service claims. No raw acquisition: it is a broad implementation library, not a decision method, and would duplicate `infra-delivery`. | MIT. Reference only. |
| [AWS official documentation](https://docs.aws.amazon.com/) | Authoritative service mechanics, policy evaluation, limits, regional support and current features | Marketing performance claims, undated price or quota figures, service-specific tutorials reproduced as guidance | AWS site terms; link and paraphrase only. |
| Optional read-only AWS MCP | Account-aware inspection of resources, logs, metrics and configuration during a diagnosis | Any mutating tool, broad administrator credential, or automatic remediation | Follow the server's license and the project's MCP approval. Use least-privilege, read-only credentials; no mutation without separate release authority. |
| [AWS Well-Architected](https://docs.aws.amazon.com/wellarchitected/latest/framework/wellarchitected-framework.html) | Review dimensions, design-principle vocabulary and lens structure | Questionnaire scores presented as audit or certification; treating pillars as a complete service checklist | Reference. |

## Selection rules

- Use these sources to deepen a decision, not to replace it. The method owns the common AWS decisions and the evidence standard.
- Do not acquire an action-heavy AWS skill raw. A skill that creates issues, mutates accounts, runs remediation or assumes administrator access crosses the release and security boundaries this collection keeps separate.
- Do not reproduce all AWS services. Cover the common 80% here and route the long tail to current service documentation and the selected stack guidance.
- Do not copy provider versions, module pins, prices, quotas, free-tier limits or regional availability into durable guidance. Verify at use time and record the date and source when a number matters.
- Keep AWS-specific service names out of provider-neutral methods; this skill is the correct home for them.
- An optional MCP server is a tool, not authority. Its read-only mode and credential scope must be verified, and a query result is evidence about the account at that moment, not a design or compliance conclusion.

## Primary references by concern

| Concern | Reference |
| --- | --- |
| Review lens | [Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/wellarchitected-framework.html) |
| Identity | [IAM best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) |
| Network | [VPC overview](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) |
| Containers | [ECS best practices](https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/intro.html), [EKS user guide](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html), [EKS best practices](https://docs.aws.amazon.com/eks/latest/best-practices/) |
| Relational data | [RDS user guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html), [Aurora high availability](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html) |
| Object storage | [S3 user guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html), [S3 durability](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DataDurability.html) |
| Messaging | [SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html), [SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) |
| Observability and cost | [CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html), [Cost Explorer](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-what-is.html), [tagging best practices](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) |
| Continuity and edge | [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html), [Route 53 routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html), [WAF](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html) |
| Secrets | [Secrets Manager rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html) |
| Optional MCP | [awslabs/mcp](https://github.com/awslabs/mcp) |

## Evidence limits

- Documentation reachability and current wording were checked; behavior was not exercised in an AWS account.
- License and repository structure were checked for the two reference repositories; their internal examples, tests and provider compatibility were not audited.
- Prices, quotas, free tiers and regional feature availability were deliberately not asserted. Any such statement in a design record needs a current source and date.
- A reference repository may change after the checked date. Re-check before relying on a specific file, path or feature.
