from flask import Flask, render_template

app = Flask(__name__)

# --- Mock Data Function ---
def get_mock_ai_news():
    """
    Generates a list of 15 mock AI news items with required fields and categories.
    """
    news_data = [
        {
            'title': 'GPT-5 Rumors: New Capabilities and Training Data',
            'summary': 'Speculation is mounting over the release of OpenAI\'s next model, focusing on multimodal input and reasoning improvements.',
            'source': 'The AI Observer',
            'link': '#',
            'category': 'LLMs & GPT'
        },
        {
            'title': 'EU Parliament Passes Landmark AI Act Regulation',
            'summary': 'The new policy establishes strict rules for high-risk AI applications and promotes transparency in foundation models.',
            'source': 'Global Policy Wire',
            'link': '#',
            'category': 'AI Ethics & Policy'
        },
        {
            'title': 'New Algorithm Boosts Real-Time Object Recognition Speed',
            'summary': 'Researchers demonstrate a breakthrough in computer vision, achieving significant FPS gains without compromising accuracy.',
            'source': 'Vision Journal',
            'link': '#',
            'category': 'Computer Vision'
        },
        {
            'title': 'Boston Dynamics Unveils Agility Improvements in New Atlas Robot',
            'summary': 'The humanoid robot now navigates complex environments with enhanced balance and precision, moving closer to practical application.',
            'source': 'Tech Robotics Daily',
            'link': '#',
            'category': 'Robotics'
        },
        {
            'title': 'The Economic Impact of Generative AI on Creative Industries',
            'summary': 'A new report analyzes the job market shifts caused by diffusion models and large language models.',
            'source': 'Future Trends Institute',
            'link': '#',
            'category': 'LLMs & GPT'
        },
        {
            'title': 'Concerns Rise Over Deepfake Detection Capabilities',
            'summary': 'Experts warn that the rapid advancement of synthesis technology is outpacing the tools designed to identify malicious content.',
            'source': 'Digital Security Weekly',
            'link': '#',
            'category': 'AI Ethics & Policy'
        },
        {
            'title': 'Vision Transformers Outperform CNNs in Medical Imaging',
            'summary': 'A study shows that ViTs provide superior diagnostic accuracy when analyzing high-resolution medical scans.',
            'source': 'Health AI News',
            'link': '#',
            'category': 'Computer Vision'
        },
        {
            'title': 'Warehouse Automation Rises with Collaborative Robot Adoption',
            'summary': 'Small and medium businesses are starting to deploy CoBots for sorting and logistics, dramatically improving efficiency.',
            'source': 'Supply Chain Today',
            'link': '#',
            'category': 'Robotics'
        },
        {
            'title': 'Microsoft Integrates Custom GPTs into Office Suite',
            'summary': 'Users can now create specialized AI assistants within Word, Excel, and PowerPoint for enhanced productivity.',
            'source': 'Redmond Insider',
            'link': '#',
            'category': 'LLMs & GPT'
        },
        {
            'title': 'Call for Global AI Moratorium on Autonomous Weapons',
            'summary': 'NGOs lobby the UN to establish a binding treaty limiting the development of lethal autonomous weapon systems.',
            'source': 'World Peace Forum',
            'link': '#',
            'category': 'AI Ethics & Policy'
        },
        {
            'title': 'Advancements in 3D Reconstruction from Single Images',
            'summary': 'New techniques allow for highly accurate depth mapping and model generation using only a single 2D photograph.',
            'source': 'Image Processing Monthly',
            'link': '#',
            'category': 'Computer Vision'
        },
        {
            'title': 'NASA Prepares to Deploy AI-Powered Rovers to Mars',
            'summary': 'The next generation of planetary explorers will use sophisticated AI for real-time decision-making and scientific analysis.',
            'source': 'Space Exploration Today',
            'link': '#',
            'category': 'Robotics'
        },
        {
            'title': 'New Open Source Llama Model Released',
            'summary': 'The community hails the new lightweight but powerful language model for its accessibility and strong performance.',
            'source': 'Hacker News',
            'link': '#',
            'category': 'LLMs & GPT'
        },
        {
            'title': 'Bias Detection Tool Released for Commercial AI Systems',
            'summary': 'A new open-source library helps developers audit their models for unfair and discriminatory outcomes.',
            'source': 'Fairness in AI',
            'link': '#',
            'category': 'AI Ethics & Policy'
        },
        {
            'title': 'Autonomous Driving Relies on Advanced Sensor Fusion',
            'summary': 'The future of L5 self-driving hinges on seamlessly combining LiDAR, camera, and radar data in real-time.',
            'source': 'Auto Tech Review',
            'link': '#',
            'category': 'Computer Vision'
        }
    ]
    return news_data

# --- Flask Routes ---
@app.route('/')
def index():
    """
    Renders the main news aggregator page.
    """
    news_items = get_mock_ai_news()

    # Get unique categories for filtering
    categories = sorted(list(set(item['category'] for item in news_items)))

    return render_template('index.html', news_items=news_items, categories=categories)

if __name__ == '__main__':
    # When running on Replit, the host should be '0.0.0.0' and port is typically 8080
    app.run(host='0.0.0.0', port=8080, debug=True)
