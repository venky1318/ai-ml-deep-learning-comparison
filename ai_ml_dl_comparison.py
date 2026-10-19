
"""
Task 10: AI vs ML vs Deep Learning
"""


def display_comparison():
    comparison = [
        {
            "feature": "Meaning",
            "AI": "Making machines perform intelligent tasks",
            "ML": "Learning patterns from data",
            "DL": "Learning using multilayer neural networks",
        },
        {
            "feature": "Scope",
            "AI": "Broad field",
            "ML": "Subset of AI",
            "DL": "Subset of ML",
        },
        {
            "feature": "How it works",
            "AI": "Rules, search, planning, or learning",
            "ML": "Algorithms learn patterns from examples",
            "DL": "Neural networks learn layered representations",
        },
        {
            "feature": "Data needs",
            "AI": "Depends on the approach",
            "ML": "Usually needs training data",
            "DL": "Often benefits from large datasets",
        },
        {
            "feature": "Example",
            "AI": "Rule-based expert system",
            "ML": "Email spam classifier",
            "DL": "Image recognition neural network",
        },
    ]

    print("\n" + "=" * 95)
    print("                 AI vs MACHINE LEARNING vs DEEP LEARNING")
    print("=" * 95)

    print(
        f"{'FEATURE':<18}"
        f"{'ARTIFICIAL INTELLIGENCE':<30}"
        f"{'MACHINE LEARNING':<25}"
        f"{'DEEP LEARNING':<22}"
    )
    print("-" * 95)

    for row in comparison:
        print(
            f"{row['feature']:<18}"
            f"{row['AI']:<30}"
            f"{row['ML']:<25}"
            f"{row['DL']:<22}"
        )

    print("-" * 95)


def display_definitions():
    print("\n1. ARTIFICIAL INTELLIGENCE (AI)")
    print(
        "AI is the broad field of building systems that perform tasks "
        "normally associated with human intelligence, such as reasoning, "
        "planning, problem-solving, and understanding language."
    )

    print("\n2. MACHINE LEARNING (ML)")
    print(
        "ML is a subset of AI in which algorithms learn patterns from "
        "data to make predictions or decisions instead of relying only "
        "on explicitly written rules."
    )

    print("\n3. DEEP LEARNING (DL)")
    print(
        "DL is a subset of ML that uses neural networks with multiple "
        "layers to learn complex patterns from data."
    )


def display_examples():
    examples = {
        "Artificial Intelligence": [
            "Rule-based expert systems",
            "Planning and search systems",
            "Game-playing systems",
        ],
        "Machine Learning": [
            "Email spam detection",
            "Product recommendation systems",
            "Sales forecasting",
        ],
        "Deep Learning": [
            "Image and facial recognition",
            "Speech recognition",
            "Neural machine translation",
        ],
    }

    print("\n4. REAL-WORLD EXAMPLES")

    for category, items in examples.items():
        print(f"\n{category}:")
        for item in items:
            print(f"  - {item}")


def display_relationship():
    print("\n5. HOW AI, ML, AND DEEP LEARNING ARE RELATED")
    print("-" * 55)
    print("Artificial Intelligence (AI)")
    print("    └── Machine Learning (ML)")
    print("          └── Deep Learning (DL)")

    print(
        "\nAI is the broader field. ML is one approach within AI, "
        "and DL is a specialized approach within ML."
    )

    print(
        "\nImportant: Not every AI system uses machine learning, "
        "and not every ML system uses deep learning."
    )


def display_conclusion():
    print("\n6. CONCLUSION")
    print(
        "AI focuses on intelligent behavior, ML enables systems to learn "
        "from data, and DL uses multilayer neural networks to learn "
        "complex representations. These concepts are related but are "
        "not interchangeable."
    )


def main():
    print("\nTASK 10: AI vs ML vs DEEP LEARNING")
    print("Veda Technology - AI & ML Internship")

    display_comparison()
    display_definitions()
    display_examples()
    display_relationship()
    display_conclusion()

    print("\nProject completed successfully.")


if __name__ == "__main__":
    main()
