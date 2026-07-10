from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib import colors

NAVY = colors.HexColor('#0a1830')
GOLD = colors.HexColor('#a5822f')
GREY = colors.HexColor('#5a6270')
BODY = colors.HexColor('#222222')
BULLET = colors.HexColor('#2a2a2a')

styles = getSampleStyleSheet()

styles.add(ParagraphStyle('CVName', fontName='Helvetica-Bold', fontSize=22, leading=26,
                           textColor=NAVY, spaceAfter=2))
styles.add(ParagraphStyle('Headline', fontName='Helvetica-Oblique', fontSize=10, leading=13,
                           textColor=GOLD, spaceAfter=4))
styles.add(ParagraphStyle('Contact', fontName='Helvetica', fontSize=9.5, leading=12,
                           textColor=GREY, spaceAfter=8))
styles.add(ParagraphStyle('SectionHead', fontName='Helvetica-Bold', fontSize=11.5, leading=14,
                           textColor=NAVY, spaceBefore=14, spaceAfter=5))
styles.add(ParagraphStyle('CVBody', fontName='Helvetica', fontSize=9.7, leading=13.5,
                           textColor=BODY, spaceAfter=6, alignment=TA_LEFT))
styles.add(ParagraphStyle('Competencies', fontName='Helvetica', fontSize=9, leading=12.5,
                           textColor=GREY, spaceAfter=4))
styles.add(ParagraphStyle('JobTitle', fontName='Helvetica-Bold', fontSize=10.5, leading=13,
                           textColor=NAVY, spaceBefore=8, spaceAfter=1))
styles.add(ParagraphStyle('JobMeta', fontName='Helvetica-Oblique', fontSize=9, leading=11.5,
                           textColor=GOLD, spaceAfter=3))
styles.add(ParagraphStyle('CVBullet', fontName='Helvetica', fontSize=9.3, leading=12.8,
                           textColor=BULLET, leftIndent=12, bulletIndent=0, spaceAfter=2))
styles.add(ParagraphStyle('SkillLine', fontName='Helvetica', fontSize=9.3, leading=13,
                           textColor=BULLET, spaceAfter=4))

doc = SimpleDocTemplate('Sebastian_Ruiz_CV.pdf', pagesize=letter,
                         topMargin=0.6 * inch, bottomMargin=0.6 * inch,
                         leftMargin=0.6 * inch, rightMargin=0.6 * inch)

story = []

story.append(Paragraph('Sebastian Ruiz', styles['CVName']))
story.append(Paragraph(
    'Head of Sales | Bilingual (EN/ES) Sales &amp; Business Development Leader | '
    'LATAM | AI-Driven Operations', styles['Headline']))
story.append(Paragraph(
    'sebastianrmconsulting@gmail.com &nbsp;|&nbsp; +57 350 205 3147 &nbsp;|&nbsp; '
    'linkedin.com/in/juansruiz11 &nbsp;|&nbsp; Colombia (Remote)', styles['Contact']))
story.append(HRFlowable(width='100%', thickness=1.2, color=GOLD, spaceAfter=6))

story.append(Paragraph('SUMMARY', styles['SectionHead']))
story.append(HRFlowable(width='100%', thickness=0.5, color=colors.HexColor('#d5d5d5'), spaceAfter=6))
story.append(Paragraph(
    "Bilingual (English/Spanish) sales and business development leader with 7+ years scaling revenue "
    "across US and LATAM markets. Generated $760K-$950K+ in placement revenue and grew customer base "
    "200% as Head of Sales at Thankz Global Staffing, then used agentic AI workflows to compress an "
    "8-person SDR operation into a lean 2-person team running at 75% higher efficiency, and expanded "
    "operations into 14 countries. Brokered $70.6M+ in international medical supply sales and advised "
    "on Colombian government contracting and trade agreements (Mercosur, EU). Hands-on AI operator: "
    "deploys AI-driven prospecting stacks and builds AI agents, automations, and internal tools.",
    styles['CVBody']))

story.append(Paragraph('CORE COMPETENCIES', styles['SectionHead']))
story.append(HRFlowable(width='100%', thickness=0.5, color=colors.HexColor('#d5d5d5'), spaceAfter=6))
story.append(Paragraph(
    "Revenue Growth Strategy | AI-Driven Team Efficiency (8 to 2 SDRs) | Outbound &amp; Pipeline Development "
    "| International Trade &amp; Government Contracting | AI-Driven Sales Operations | "
    "CRM (HubSpot, Apollo, ZoomInfo) | LinkedIn Social Selling | Cross-Cultural Negotiation (EN/ES)",
    styles['Competencies']))

story.append(Paragraph('EXPERIENCE', styles['SectionHead']))
story.append(HRFlowable(width='100%', thickness=0.5, color=colors.HexColor('#d5d5d5'), spaceAfter=6))

jobs = [
    ("Head of Sales", "Thankz Global Staffing, Los Angeles (Remote from LATAM)", "Mar 2021 - Present", [
        "Generated $760K-$950K+ in placement revenue, growing the customer base 200% through 30+ specialized AI and finance talent placements.",
        "Managed end-to-end SDR operations and training, introducing agentic AI workflows that drove a 75% increase in operational efficiency, enabling a lean 2-person team to handle the output of a traditional 8-person SDR org.",
        "Spearheaded expansion into 14 countries, establishing new operations and client bases.",
        "Deployed an AI-driven sales stack (Jasper, Apollo, Reply.io) alongside HubSpot, Tracker RMS, ZoomInfo, and Waalaxy, scaling outbound efficiency.",
        "Built LinkedIn into the company's #1 new-business channel through organic authority and outbound strategy.",
    ]),
    ("Founder &amp; Airbnb Coach (Part-Time)", "77Rentals, Colombia", "2022 - Present", [
        "Built AI-powered hosting management software and a guest-experience platform from the ground up.",
        "Operate 3 short-term rental properties; coach new Airbnb hosts through a course and guide software.",
        "Design and deploy AI agents and automation workflows for guest communication, operations, and reporting.",
    ]),
    ("Global Trade Consultant", "SM Consulting, Bogot&aacute;, Colombia", "Apr 2020 - Dec 2023", [
        "Brokered and facilitated $70.6M+ in medical supply sales (3M masks, surgical gloves) during the global PPE shortage, connecting Chinese and Korean manufacturers with buyers in Colombia, the US, and Qatar.",
        "Advised startups on business development, client acquisition, Colombian government contracting, and US market entry.",
        "Built a global supplier and buyer network across China, USA, and India through cold outreach, email, and LinkedIn.",
    ]),
    ("Sales Manager", "Virtual Emily, Miami, FL", "Oct 2020 - Mar 2021", [
        "Drove sales growth across 5 business lines in the US market.",
        "Built a robust pipeline in HubSpot CRM via multi-channel outbound (cold calling, email, LinkedIn).",
        "Ran client meetings end to end, converting prospects into new business wins.",
    ]),
    ("Operations Manager", "Hunter Logistix, Miami, FL", "Jan 2019 - May 2020", [
        "Coordinated dispatch operations across multiple US states for owner-operators, working closely with US DOTs to keep freight moving through COVID-19 lockdowns.",
        "Generated ROI reports and route analytics to optimize logistics strategy.",
        "Attracted new B2B clients through HubSpot CRM-driven prospecting.",
    ]),
    ("Logistics Manager", "Xtrategy Logistics, Tampa, FL", "Jan 2019 - Nov 2019", [
        "Executed a high-profile Silicon Valley mission with the Medell&iacute;n Chamber of Commerce, bringing presidents and HR VPs of Colombia's largest companies to Google, Meta, Amazon, and LinkedIn (65 executives).",
        "Authored investor reports on Colombian economic policy, law, and commercial agreements.",
        "Analyzed trade agreements between Colombia, Mercosur countries, and the EU.",
    ]),
    ("Business Development", "Vitae Spiritz, Shanghai, China", "May 2018 - Sep 2018", [
        "Represented Colombian brands at trade events and industry association meetings across China.",
        "Built digital presence on Taobao and WeChat for the Chinese market.",
        "Developed targeted marketing and sales strategies for multiple brands entering China.",
    ]),
]

for title, org, dates, bullets in jobs:
    story.append(Paragraph(f'{title} &nbsp;|&nbsp; {org}', styles['JobTitle']))
    story.append(Paragraph(dates, styles['JobMeta']))
    for b in bullets:
        story.append(Paragraph(f'- {b}', styles['CVBullet']))

story.append(Paragraph('EDUCATION', styles['SectionHead']))
story.append(HRFlowable(width='100%', thickness=0.5, color=colors.HexColor('#d5d5d5'), spaceAfter=6))
story.append(Paragraph('<b>MBA (On Pause)</b>, Indiana Tech, Fort Wayne, Indiana, expected 2028', styles['CVBody']))
story.append(Paragraph(
    "<b>Bachelor of Science in Entrepreneurship &amp; International Business</b>, Minor in Criminology, "
    'The University of Tampa, 2019, Honors Graduate', styles['CVBody']))

story.append(Paragraph('SKILLS', styles['SectionHead']))
story.append(HRFlowable(width='100%', thickness=0.5, color=colors.HexColor('#d5d5d5'), spaceAfter=6))
skills = [
    ("Sales &amp; Leadership", "team leadership (8 SDRs), negotiation and deal closing, pipeline management and forecasting, client acquisition, B2B strategy, contract management"),
    ("AI &amp; Tools", "AI-driven sales workflows (ChatGPT, Claude, Jasper), AI agents and automation building, HubSpot, Apollo, ZoomInfo, Reply.io, Waalaxy, no-code product building, data visualization"),
    ("International Trade", "Colombian government contracting, trade agreements (Mercosur, EU), US and LATAM market entry, import/export brokering, economic and policy research"),
    ("Languages", "Spanish (Native), English (Fluent, professional)"),
]
for label, val in skills:
    story.append(Paragraph(f'<b>{label}:</b> {val}', styles['SkillLine']))

doc.build(story)
print('done')
