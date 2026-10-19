# Define a performance claim

Start from an accepted journey, target environment and demand/latency objective. State representative roles, operations, payload/data sizes, cache state and external boundaries. Label provisional thresholds; do not import a tool example as a product commitment. Distinguish offered demand, achieved throughput, incomplete/dropped work, error rate and completion latency. Request admission or a fast acknowledgement does not establish durable completion.

Choose a workload that represents the product's arrival/concurrency model; slower responses can reduce offered load in a closed model. Check that the generator actually produced the intended demand without becoming the bottleneck. Compare equivalent code/configuration, resources, fixtures and intervals; inspect service/dependency saturation and recovery as well as user outcomes.

Bound traffic, side effects, duration and cleanup to the authorized target. A shared or deployed environment needs its established action scope and stop conditions. Preserve thresholds and failure results, sanitize artifacts and identify mocked providers. Use the existing compatible performance suite or an explicitly selected tool; installed performance-testing supplies k6 mechanics when that stack is accepted. Combining load with a fault is a separately scoped experiment.
