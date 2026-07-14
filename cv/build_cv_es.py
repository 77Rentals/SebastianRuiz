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

doc = SimpleDocTemplate('Sebastian_Ruiz_CV_ES.pdf', pagesize=letter,
                         topMargin=0.6 * inch, bottomMargin=0.6 * inch,
                         leftMargin=0.6 * inch, rightMargin=0.6 * inch)

story = []

story.append(Paragraph('Sebastian Ruiz', styles['CVName']))
story.append(Paragraph(
    'Head of Sales | L&iacute;der Biling&uuml;e (EN/ES) de Ventas y Desarrollo de Negocios | '
    'LATAM | Operaciones Impulsadas por IA', styles['Headline']))
story.append(Paragraph(
    '<link href="https://sebastianruiz.online/" color="#a5822f">https://sebastianruiz.online/</link> &nbsp;|&nbsp; '
    'sebastianrmconsulting@gmail.com &nbsp;|&nbsp; +57 350 205 3147 &nbsp;|&nbsp; '
    'linkedin.com/in/juansruiz11 &nbsp;|&nbsp; Colombia (Remote)', styles['Contact']))
story.append(HRFlowable(width='100%', thickness=1.2, color=GOLD, spaceAfter=6))

story.append(Paragraph('RESUMEN', styles['SectionHead']))
story.append(HRFlowable(width='100%', thickness=0.5, color=colors.HexColor('#d5d5d5'), spaceAfter=6))
story.append(Paragraph(
    "L&iacute;der biling&uuml;e (ingl&eacute;s/espa&ntilde;ol) de ventas y desarrollo de negocios con "
    "m&aacute;s de 7 a&ntilde;os escalando ingresos en los mercados de EE. UU. y LATAM. Gener&eacute; "
    "entre $760K y $950K+ en ingresos por colocaci&oacute;n y crec&iacute; la base de clientes 200% "
    "como Head of Sales en Thankz Global Staffing, luego us&eacute; flujos de trabajo de IA agentiva "
    "para reducir un equipo de SDR de 8 personas a un equipo &aacute;gil de 2 personas operando con un "
    "75% m&aacute;s de eficiencia, y expand&iacute; operaciones a 14 pa&iacute;ses. Gestion&eacute; "
    "m&aacute;s de $70.6M en ventas internacionales de insumos m&eacute;dicos y asesor&eacute; sobre "
    "acuerdos comerciales (Mercosur, UE). Operador pr&aacute;ctico de IA: implementa stacks de "
    "prospecci&oacute;n impulsados por IA y construye agentes de IA, automatizaciones y herramientas internas.",
    styles['CVBody']))

story.append(Paragraph('COMPETENCIAS CLAVE', styles['SectionHead']))
story.append(HRFlowable(width='100%', thickness=0.5, color=colors.HexColor('#d5d5d5'), spaceAfter=6))
story.append(Paragraph(
    "Estrategia de Crecimiento de Ingresos | Eficiencia de Equipo Impulsada por IA (8 a 2 SDRs) | "
    "Desarrollo de Prospecci&oacute;n y Pipeline | Comercio Internacional | Operaciones de Ventas "
    "Impulsadas por IA | CRM (HubSpot, Apollo, ZoomInfo) | Venta Social en LinkedIn | "
    "Negociaci&oacute;n Intercultural (EN/ES)",
    styles['Competencies']))

story.append(Paragraph('EXPERIENCIA', styles['SectionHead']))
story.append(HRFlowable(width='100%', thickness=0.5, color=colors.HexColor('#d5d5d5'), spaceAfter=6))

jobs = [
    ("Head of Sales", "Thankz Global Staffing, Los &Aacute;ngeles (Remoto desde LATAM)", "Mar 2021 - Presente", [
        "Gener&eacute; entre $760K y $950K+ en ingresos por colocaci&oacute;n, creciendo la base de clientes 200% mediante m&aacute;s de 30 colocaciones especializadas de talento en IA y finanzas.",
        "Gestion&eacute; operaciones y capacitaci&oacute;n de SDR de principio a fin, introduciendo flujos de trabajo de IA agentiva que impulsaron un aumento del 75% en eficiencia operativa, permitiendo que un equipo &aacute;gil de 2 personas manejara el rendimiento de un equipo tradicional de 8 SDRs.",
        "Lider&eacute; la expansi&oacute;n a 14 pa&iacute;ses, estableciendo nuevas operaciones y bases de clientes.",
        "Implement&eacute; un stack de ventas impulsado por IA (Jasper, Apollo, Reply.io) junto con HubSpot, Tracker RMS, ZoomInfo y Waalaxy, escalando la eficiencia de prospecci&oacute;n saliente.",
        "Convert&iacute; a LinkedIn en el canal n&uacute;mero 1 de nuevos negocios de la empresa mediante autoridad org&aacute;nica y estrategia de prospecci&oacute;n.",
    ]),
    ("Fundador &amp; Airbnb Coach (Medio Tiempo)", "77Rentals, Colombia", "2022 - Presente", [
        "Constru&iacute; desde cero un software de gesti&oacute;n de hospedaje impulsado por IA y una plataforma de experiencia para hu&eacute;spedes.",
        "Opero 3 propiedades de alquiler de corta estad&iacute;a; asesoro a nuevos anfitriones de Airbnb mediante un curso y un software gu&iacute;a.",
        "Dise&ntilde;o e implemento agentes de IA y flujos de automatizaci&oacute;n para comunicaci&oacute;n con hu&eacute;spedes, operaciones y reportes.",
    ]),
    ("Consultor de Comercio Global", "SM Consulting, Bogot&aacute;, Colombia", "Abr 2020 - Dic 2023", [
        "Gestion&eacute; y facilit&eacute; m&aacute;s de $70.6M en ventas de insumos m&eacute;dicos (3M tapabocas, guantes quir&uacute;rgicos) durante la escasez global de EPP, conectando fabricantes chinos y coreanos con compradores en Colombia, EE. UU. y Catar.",
        "Asesor&eacute; a startups en desarrollo de negocios, adquisici&oacute;n de clientes y entrada al mercado de EE. UU.",
        "Constru&iacute; una red global de proveedores y compradores en China, EE. UU. e India mediante prospecci&oacute;n en fr&iacute;o, correo electr&oacute;nico y LinkedIn.",
    ]),
    ("Gerente de Ventas", "Virtual Emily, Miami, FL", "Oct 2020 - Mar 2021", [
        "Impuls&eacute; el crecimiento de ventas en 5 l&iacute;neas de negocio en el mercado de EE. UU.",
        "Constru&iacute; un pipeline s&oacute;lido en CRM HubSpot mediante prospecci&oacute;n multicanal (llamadas en fr&iacute;o, correo electr&oacute;nico, LinkedIn).",
        "Gestion&eacute; reuniones con clientes de principio a fin, convirtiendo prospectos en nuevos negocios.",
    ]),
    ("Gerente de Operaciones", "Hunter Logistix, Miami, FL", "Ene 2019 - May 2020", [
        "Coordin&eacute; operaciones de despacho en m&uacute;ltiples estados de EE. UU. para propietarios-operadores, trabajando estrechamente con los DOT de EE. UU. para mantener el flujo de carga durante los confinamientos por COVID-19.",
        "Gener&eacute; reportes de ROI y an&aacute;lisis de rutas para optimizar la estrategia log&iacute;stica.",
        "Atra&iacute;a nuevos clientes B2B mediante prospecci&oacute;n impulsada por CRM HubSpot.",
    ]),
    ("Gerente de Log&iacute;stica", "Xtrategy Logistics, Tampa, FL", "Ene 2019 - Nov 2019", [
        "Ejecut&eacute; una misi&oacute;n de alto perfil a Silicon Valley con la C&aacute;mara de Comercio de Medell&iacute;n, llevando a presidentes y vicepresidentes de RR. HH. de las empresas m&aacute;s grandes de Colombia a Google, Meta, Amazon y LinkedIn (65 ejecutivos).",
        "Redact&eacute; informes para inversionistas sobre pol&iacute;tica econ&oacute;mica, legislaci&oacute;n y acuerdos comerciales de Colombia.",
        "Analic&eacute; acuerdos comerciales entre Colombia, los pa&iacute;ses del Mercosur y la UE.",
    ]),
    ("Desarrollo de Negocios", "Vitae Spiritz, Shangh&aacute;i, China", "May 2018 - Sep 2018", [
        "Represent&eacute; a marcas colombianas en eventos comerciales y reuniones de asociaciones industriales en toda China.",
        "Constru&iacute; presencia digital en Taobao y WeChat para el mercado chino.",
        "Desarroll&eacute; estrategias de marketing y ventas dirigidas para m&uacute;ltiples marcas que ingresaban a China.",
    ]),
]

for title, org, dates, bullets in jobs:
    story.append(Paragraph(f'{title} &nbsp;|&nbsp; {org}', styles['JobTitle']))
    story.append(Paragraph(dates, styles['JobMeta']))
    for b in bullets:
        story.append(Paragraph(f'- {b}', styles['CVBullet']))

story.append(Paragraph('EDUCACI&Oacute;N', styles['SectionHead']))
story.append(HRFlowable(width='100%', thickness=0.5, color=colors.HexColor('#d5d5d5'), spaceAfter=6))
story.append(Paragraph('<b>MBA (En Pausa)</b>, Indiana Tech, Fort Wayne, Indiana, prevista para 2028', styles['CVBody']))
story.append(Paragraph(
    "<b>Bachelor of Science in Entrepreneurship &amp; International Business</b>, Minor en Criminolog&iacute;a, "
    'The University of Tampa, 2019, Graduado con Honores', styles['CVBody']))

story.append(Paragraph('HABILIDADES', styles['SectionHead']))
story.append(HRFlowable(width='100%', thickness=0.5, color=colors.HexColor('#d5d5d5'), spaceAfter=6))
skills = [
    ("Ventas y Liderazgo", "liderazgo de equipos (8 SDRs), negociaci&oacute;n y cierre de negocios, gesti&oacute;n y pron&oacute;stico de pipeline, adquisici&oacute;n de clientes, estrategia B2B, gesti&oacute;n de contratos"),
    ("IA y Herramientas", "flujos de ventas impulsados por IA (Claude, Jasper), automatizaci&oacute;n de flujos de trabajo agentivos (Zapier, Make, n8n), ingenier&iacute;a de prompts y orquestaci&oacute;n de LLM, RAG y herramientas internas de conocimiento, desarrollo con Claude API y Claude Code, HubSpot, Apollo, ZoomInfo, Reply.io, Waalaxy, construcci&oacute;n de productos no-code, visualizaci&oacute;n de datos"),
    ("Comercio Internacional", "acuerdos comerciales (Mercosur, UE), entrada al mercado de EE. UU. y LATAM, intermediaci&oacute;n de importaci&oacute;n/exportaci&oacute;n, investigaci&oacute;n econ&oacute;mica y de pol&iacute;ticas p&uacute;blicas"),
    ("Idiomas", "Espa&ntilde;ol (Nativo), Ingl&eacute;s (Fluido, profesional)"),
]
for label, val in skills:
    story.append(Paragraph(f'<b>{label}:</b> {val}', styles['SkillLine']))

doc.build(story)
print('done')
