```mermaid
flowchart LR
    A[Upload Image] --> B[Preprocess Image]
    B --> C[Analyze Image]
    C --> D[Classify Acne Type]
    D --> E[Show Result]
    E --> F[Save Report]
