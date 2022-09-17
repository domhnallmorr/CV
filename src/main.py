import pandas as pd
import streamlit as st

import images

blade_image, neo_image, riser_image, flexcom_image, psu_image = images.setup_images()

st.set_page_config(layout="wide")

tabs_font_css = """
<style>
button[data-baseweb="tab"] {
  font-size: 26px;
}
</style>
"""
st.write(tabs_font_css, unsafe_allow_html=True)
st.header("Domhnall Morrissey CV")
tab1, tab2, tab3 = st.tabs(["About Me", "Employment History", "Skills/Experience Overview"])

with tab1:
	st.subheader("About Me")
	st.write("I am an engineer with 11 years experience in the aerospace and oil and gas industries")
	st.write("Experience in FE analysis of aircraft structures (utilising NASTRAN) and offshore structures (utilising Flexcom/Deepriser)")
	st.write("Experience in Part 21 DOA cabin reconfigurations")
	st.write("Keen interest in programming (Python)")
	st.write("This app is written in the python module streamlit. Details of my experience and skills are detailed throughout")
	st.write("For further information on streamlit, see https://streamlit.io/")
	
	st.subheader("Personal Details")
	st.markdown("Current Role: Senior Stress Engineer, Spirit Aerosystems, Belfast, UK")
	st.markdown("Nationality: Irish")

	'''
		![Repo](https://img.icons8.com/color/48/000000/new-post.png) domhnallmorr@yahoo.co.uk

	'''
	
	'''
		[![Repo](https://img.icons8.com/color/48/000000/linkedin-circled--v1.png)](https://github.com/domhnallmorr) https://www.linkedin.com/in/domhnall-morrissey-1599b416/

	'''

	'''
		[![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/domhnallmorr) https://github.com/domhnallmorr

	'''
	st.markdown("<br>",unsafe_allow_html=True)

	col1, col2 = st.columns([1, 5])
	
	with col1:
		'''
			![Repo](https://img.icons8.com/external-prettycons-lineal-color-prettycons/49/000000/external-university-education-prettycons-lineal-color-prettycons.png) Qualifications

		'''
		st.markdown("<br>",unsafe_allow_html=True)

	with col2:
		st.write("- Bachelor’s degree in Aeronautical Engineering (Honours – 2nd Class), University of Limerick, 2005 - 2009")
		st.write("- MSc Aerospace Engineering at Swansea University , Swansea University, 2009 - 2010")

	st.subheader("Employment History")
	df = pd.DataFrame(
					[["Airbus UK", "Wing GFEM Analyst", "Bristol, UK", "April 2011 to November 2016"],
					["Eirtech Aviation", "Design Engineer", "Shannon, Ireland", "November 2016 to June 2018"],
					["Wood PLC", "Senior Engineer", "Galway, Ireland", "June 2018 to August 2022"],
					["Spirit Aerosystems", "Senior Stress Engineer", "Belfast, UK", "August 2022 to Present"]],
					columns=["Company", "Role", "Location", "Dates"])
	
	st.write("See Employment History tab for full details")
	st.table(df)
	
with tab2:
	# ################# AIRBUS #################
	with st.expander("Airbus UK - Wing GFEM Analyst - April 2011 to November 2016 - Bristol, UK"):
		st.markdown("#### **Role Duties**")
		st.markdown("- FEA analysis of wing global models")
		st.markdown("- Updating models based on latest sizing/geometry updates from stress and design teams")
		st.markdown("- Preparation of Nastran load cards based on data from flight physics team")
		st.markdown("- Preparation of results for stress and systems (fuel and landing gear) teams")
		st.markdown("- Presentation of results at quality reviews")
		
		st.markdown("#### **Skills Developed**")
		st.markdown("- FEA Solver: NASTRAN")
		st.markdown("- FEA Preprocessor: NASTRAN/Hyperworks")
		st.markdown("- Automation of processes through MATLAB scripts")
		st.markdown("- Mentoring contractors and graduates")
		
		st.markdown("#### **Notable Projects**")
		
		# #### BLADE ####
		col1, col2 = st.columns(2)
		with col1:
			st.image(blade_image)
			
		with col2:
			st.markdown("### A340 BLADE")
			st.markdown("- Breakthrough Laminar Aircraft Demonstrator in Europe (BLADE)")
			st.markdown("- Laminar flow wing section applied to the outer wing of a A340 test aircraft")
			st.markdown("- Developed GFEM of laminar flow section to be included in existing A340 wing GFEM")
			st.markdown("- Managed geomtry and sizing changes throughout program")

		# #### A330 NEO ####
		col1, col2 = st.columns(2)	
		
		with col1:
			st.image(neo_image)
			
		with col2:
			st.markdown("### A330 NEO")
			st.markdown("### New engines and rework of wingtip region")
			st.markdown("- Team lead for A330 NEO activities")
			st.markdown("- Involved in early sensitivity studies of possible revised winglet loads through until certification model GFEM")
			st.markdown("- Application of geometry updates from CEO (current engine option) wing")
			st.markdown("- Management of sizing updates throughout program")


	# ################# EIRTECH #################
	with st.expander("Eirtech Aviation - Design Engineer - November 2016 to June 2018 - Shannon, Ireland"):
		col1, col2 = st.columns([5,4])
		
		with col1:
			st.markdown("#### **Role Duties**")
			st.markdown("- Provide engineering documentation and materials for aircraft cabin reconfigurations")
			st.markdown("- Preparation of documentation such as Service Bulletins")
			st.markdown("- Preparation of engineering drawings")
			st.markdown("- Preparation of Bill of Materials (BOM)")
			st.markdown("- Liaison with clients")
			
			st.markdown("#### **Skills Developed**")
			st.markdown("- AutoCAD 2d drawings")
			st.markdown("- LOPAs")
			st.markdown("- PSU layouts")
			st.markdown("- EELs")
			st.markdown("- Placard Kits")
			st.markdown("- A320 OHSC Installation")
	
		with col2:
			st.markdown("Example PSU drawing generated by PYCabin software")
			st.image(psu_image)

	# ################# WOOD #################
	with st.expander("Wood PLC - Senior Engineer - June 2018 to August 2022 - Galway, Ireland"):
		col1, col2 = st.columns([5,4])	
		
		with col1:
			st.markdown("#### **Role Duties**")
			
			st.markdown("- FEA analysis of offshore drilling risers")
			st.markdown("- Preparation of FEA models based on client inputs (e.g. vessel data, water depth, local environmental data, etc)")
			st.markdown("- Static and Dynamic FEA analysis")
			st.markdown("- Generation of operational envelopes for use by the Drilling Rig team during drilling operations")
			st.markdown("- Calculation of fatigue lives")
			st.markdown("- Preparation of technical reports detailing results and conclusions")
			
			st.subheader("Skills Developed")
			st.markdown("- FEA Solvers/Preprocessors: Deepriser/Flexcom")
			st.markdown("- VIV (Vortex Induced Vibration) Software: Shear7")
			st.markdown("- Fatigue Life Calculations")
			st.markdown("- Modal Analysis")
			st.markdown("- Environmental conditions modelling (currents, wave, wind)")
			st.markdown("- Development of python library for interacting with the FEA input/output files")
			st.markdown("- Development of python app (with streamlit) for QA of input files")
			st.markdown("- Project Management")
			
		with col2:
			st.markdown("##### Typical Drilling Riser System")
			st.image(riser_image)
			st.markdown("##### Flexcom Riser Model")
			st.image(flexcom_image)
		

		
	st.markdown(
		"""
	<style>
	.streamlit-expanderHeader {
		font-size: x-large;
	}
	</style>
	""",
		unsafe_allow_html=True,
	)

with tab3:	
	st.subheader("Skills/Experience Overview")
	
	st.markdown("#### Core Skills")
	st.write("- Finite element analysis")
	st.write("- Aircraft structures, offshore structures")
	st.write("- Project managment")
	st.write("- Mentoring of junior team members")
	st.write("- Programming (further details below)")
	st.write("- 2d CAD (AutoCAD)")
	
	st.write("_____________________________")
	st.markdown("#### Programming")
	
	col1, col2 = st.columns(2)
	with col1:
		st.markdown("Proficient in Python programming. Have utilised Python for many tasks including;")
		st.write("- File Parsing (reading input/output files)")
		st.write("- Automation of processes")
		st.write("- Processing measured data (e.g. vessel motions)")
		st.write("- QA scripts")
		st.write("- Generation of MS Excel files")
		st.write("- GUI development")
		st.write("- Desktop GUIs (see opposite for examples)")
		st.write("- Data Analytics apps (this app for example is generated using such a framework called streamlit)")
		st.write("- Basic knowledge machine learning (PyTorch)")
		st.write("- Basic knowledge web development (Django, Matrialize CSS and HTML)")
		
		
	with col2:
		st.markdown("###### PYCabin")
		st.markdown("Proof of concept app for Part 21 DOA cabin reconfiguration projects")
		st.markdown("Considers LOPAs, PSU arrangements and EEL layouts")
		st.markdown("Note, A320 only")
		st.markdown("See https://github.com/domhnallmorr/PYCabin_Tk")
		st.image(r"https://i.imgur.com/TGQvXVe.jpg")


		st.markdown("###### Tk Path Finder")
		st.markdown("File explorer being developed based on tabs within tab concept")
		st.markdown("See https://github.com/domhnallmorr/Tk-Path-Finder")
		st.image(r"https://i.imgur.com/zxXQ8hS.png")
