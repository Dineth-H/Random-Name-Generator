import tkinter as tk
import random

# Lists of prefixes and suffixes
prefixes = [
    "Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta", "Iota", "Kappa",
    "Lambda", "Mu", "Nu", "Xi", "Omicron", "Pi", "Rho", "Sigma", "Tau", "Upsilon", "Phi",
    "Chi", "Psi", "Omega", "Micro", "Nano", "Mega", "Ultra", "Super", "Hyper", "Mini", "Maxi",
    "Multi", "Inter", "Intra", "Geo", "Eco", "Auto", "Bio", "Cyber", "Info", "Techno", "Tele",
    "Neuro", "Gen", "Aero", "Eco", "Hydro", "Agro", "Electro", "Geo", "Nano", "Photo", "Synth",
    "Hyper", "Mega", "Chrono", "Crypto", "Robo", "Space", "Solar", "Terra", "Bio", "Neuro",
    "Macro", "Quantum", "Neuro", "Futuro", "Xeno", "Vivo", "Cyto", "Mito", "Para", "Astro",
    "Hyper", "Ultra", "Exo", "Pro", "Cyber", "Virtual", "Auto", "Aqua", "Aero", "Nano",
    "Arch", "Proxima", "Xeno", "Hypernova", "Bio", "Syntho", "Nucleo", "Galacto", "Spectro", "Cryo",
    "Myco", "Hydro", "Luno", "Pyro", "Nebula", "Solaris", "Cosmo", "Quantum", "Aqua", "Aero"
]

suffixes = [
    "Corp", "Inc", "Ltd", "LLC", "Group", "Technologies", "Solutions", "Industries", "Enterprises", "Systems",
    "Innovations", "Ventures", "Services", "Partners", "International", "Global", "Associates", "Enterprises", "Dynamics",
    "Consulting", "Digital", "Tech", "Analytics", "Solutions", "Labs", "Networks", "Software", "Hardware", "Electronics",
    "Web", "Media", "Consultants", "R&D", "Manufacturing", "Development", "Biotech", "Pharma", "Health", "Energy",
    "Automotive", "Aerospace", "Finance", "Bank", "Insurance", "Security", "Education", "Training", "Research",
    "Management", "Marketing", "Design", "Creative", "Studio", "Production", "Art", "Entertainment", "Broadcasting",
    "Publishing", "Communications", "Communications", "Mobile", "Wireless", "Games", "Interactive", "Media", "eCommerce",
    "Online", "Cloud", "Information", "Data", "Cyber", "AI", "Robotics", "IoT", "Blockchain", "Digital", "Sustainable",
    "Renewable", "Green", "Clean", "Solar", "Bio", "Nano", "Advanced", "Smart", "NextGen", "Virtual", "Augmented",
    "Global", "Local", "Urban", "Rural", "Luxury", "Premium", "Value", "Gold", "Silver", "Platinum", "Diamond",
    "Elite", "Exclusive", "Professional", "Expert", "Specialist", "Institute", "Foundation", "Association", "Society",
    "Union", "Federation", "Alliance", "Cooperative", "Network", "League", "Guild", "Club", "Team", "Project",
    "Initiative", "Program", "Mission", "Vision", "Foundation", "Fund", "Trust", "Endowment", "Innovation", "Center",
    "Lab", "Hub", "House", "Factory", "Plant", "Studios", "Works", "Creations", "Productions", "Inventions",
    "Manufacturers", "Co.", "Company", "Holdings", "Enterprises", "Partnerships", "Collaborative", "Collective",
    "Community", "Association", "Chamber", "Consortium", "Council", "Organization", "Agency", "Bureau", "Office",
    "Division", "Department", "Administration", "Service",
    "Venture", "Ventures", "Lab", "Labs", "Creators", "Innovators", "Designs", "Development", "Manufacturers", "Solutions",
    "Creators", "Builders", "Research", "Explorers", "Creators", "Explorations", "Enterprises", "Enterprisers", "Creators", "Productions"
]

# Function to generate random names
def generate_name():
    keyword = keyword_entry.get()
    if keyword:
        random_prefix = random.choice(prefixes)
        random_suffix = random.choice(suffixes)
        generated_name = random_prefix + " " + keyword + " " + random_suffix
        result_label.config(text=f"Generated Name: {generated_name}")
    else:
        result_label.config(text="Please enter a keyword.")

# Create the main window
root = tk.Tk()
root.title("Random Name Generator")

# Create and pack a label for instructions
instruction_label = tk.Label(root, text="Enter a keyword to generate a random name:")
instruction_label.pack()

# Create and pack an entry widget for the keyword
keyword_entry = tk.Entry(root)
keyword_entry.pack()

# Create and pack a button to generate names
generate_button = tk.Button(root, text="Generate Name", command=generate_name)
generate_button.pack()

# Create and pack a label to display the generated name
result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI main loop
root.mainloop()
