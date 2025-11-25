# Expansion and Conflict Project Step-by-Step Guide
# Written in Python 3

def wait_for_user(prompt="Press Enter when you're ready to continue..."):
    input(f"\n{prompt}")

def main():
    print("📘 Welcome to the 'Expansion and Conflict Project' Guide!\n")
    print("This program will walk you step-by-step through the project instructions.")
    wait_for_user("Are you ready to begin? Press Enter to start!")

    steps = [
        # Combined Steps 1–11
        "Step 1: Project Overview\n"
        "-----------------------------------\n"
        "You will create a PowerPoint covering the key points of the *Expansion and Conflict Unit*.\n\n"
        "Your PowerPoint should provide information and answer questions about key topics, "
        "using your own words — do NOT copy and paste from lessons or other sources.\n\n"
        "Each section of your PowerPoint represents one lesson from the unit. "
        "Separate each lesson using a **title slide**, followed by slides for each event or topic.\n\n"
        "Every slide must include:\n"
        "   • A title\n"
        "   • A picture (with a cited source)\n"
        "   • A short description (except title slides, which don’t need one)\n\n"
        "Main sections you’ll include:\n"
        "   • Expansion of Industry\n"
        "   • Immigration and Westward Expansion\n"
        "   • The Texas Revolution\n"
        "   • The Mexican American War\n"
        "   • The Gadsden Purchase\n"
        "   • Sectionalism\n\n"
        "Create one slide for each bullet point listed under these sections.",

        # Step 12 onward (lesson-specific details)
        "Step 2: Expansion of Industry — Include slides for:\n"
        "   • Impact of the Industrial Revolution on expansion\n"
        "   • Economic advances pushing expansion\n"
        "   • Three industrial advances and why they matter",

        "Step 3: Immigration and Westward Expansion — Include slides for:\n"
        "   • What is Manifest Destiny?\n"
        "   • Justifications for Manifest Destiny\n"
        "   • How immigration impacted Westward Expansion\n"
        "   • Positive and negative lasting impacts of Westward Expansion",

        "Step 4: The Texas Revolution — Include slides for:\n"
        "   • How it started\n"
        "   • What people had to do to live in Texas\n"
        "   • How long it took for Texas to become independent and then a state\n"
        "   • How the slavery divide influenced Westward Expansion",

        "Step 5: The Mexican American War — Include slides for:\n"
        "   • Tensions between the U.S. and Mexico\n"
        "   • What President Polk did before starting the war and why\n"
        "   • Lasting impact and significance of the war\n"
        "   • What the Gadsden Purchase was and why the U.S. wanted that land",

        "Step 6: Sectionalism — Include slides for:\n"
        "   • Definition and 2 differences between North and South\n"
        "   • Long-term and short-term causes of sectionalism\n"
        "   • What are States’ rights (with 2 examples)\n"
        "   • Summaries of 2 major compromises",

        "Step 7: Double-check that all writing is in your own words and that every slide includes a picture with a citation.",

        "Step 8: Review your PowerPoint for accuracy, clarity, and creativity.",

        "✅ Project Complete! Great job — you now have a full plan for your Expansion and Conflict PowerPoint!"
    ]

    for step in steps:
        print("\n" + step)
        if "✅" not in step:
            wait_for_user("Ready for the next step? Press Enter...")

    print("\n🎉 You’ve finished all the instructions! Good luck with your project!")

if __name__ == "__main__":
    main()
