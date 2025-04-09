from fpdf import FPDF


text = """
Dear Hiring Manager,

I am writing to express my interest in the <ROLE> position at <FIRM>. With 3 years of experience in full-stack web development and data science, I am confident in my ability to contribute effectively to your team.

In my professional career, I have developed and deployed scalable web applications, optimized data pipelines, and built machine learning infrastructure for a variety of use cases. As a Data Scientist at Atec Spine, I engineered machine learning pipelines to preprocess databases and developed microservices for data processing. My full-stack development experience at UCSD Health further honed my skills, where I led the creation of web applications and dashboards to streamline complex data workflows.

I am proficient in a range of modern technologies, including TypeScript, Python, C++, React, Docker, and cloud platforms like Azure and Google Cloud. My hands-on experience with both backend and frontend technologies, combined with a strong foundation in software engineering, enables me to build robust and efficient systems that meet <KIND> needs.

I am excited about the opportunity to bring my blend of technical skills, creativity, and problem-solving ability to <FIRM>. I look forward to the chance to discuss how I can contribute to your team.

Thank you for your consideration.

Sincerely,
Brian Barry
"""

if __name__ == '__main__':
    role = input('Role: ')
    firm = input('Company: ')
    kind = input('Business (default) or Organization (o)?: ')

    if kind == '':
        kind = 'business'
    else:
        kind = 'operational'
    text = text.replace('<ROLE>', role)
    text = text.replace('<FIRM>', firm)
    text = text.replace('<KIND>', kind)
    print('\n', text)

    pdf = FPDF()
    
    pdf.set_margins(left=20, top=20, right=20)
    pdf.add_page()
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, pdf.font_size * 1.15, text)

    out_path = '/Users/brianbarry/Desktop/Brian_Barry_cover_letter.pdf'
    pdf.output(out_path)