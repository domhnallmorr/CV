import streamlit as st

import images

blade_image, riser_image = images.setup_images()

st.set_page_config(layout="wide")

st.header("Domhnall Morrissey CV")
tab1, tab2, tab3 = st.tabs(["Personal Details", "Employment History", "Skills/Experience Overview"])

with tab1:
	st.subheader("Personal Details")
	
with tab2:
	st.subheader("Employment History")	
	# ################# AIRBUS #################
	with st.expander("Airbus UK - Wing GFEM Analyst - April 2011 to November 2016 - Bristol, UK"):
		st.markdown("#### **Role Duties**")
		st.markdown("- FEA analysis of wing global models")
		st.markdown("- Updating models based on latest sizing/geometry updates from stress and design teams")
		st.markdown("- Prepartion of Nastran load cards based on data from flight physics team")
		st.markdown("- Prepartion of results for stress and systems (fuel and landing gear) teams")
		st.markdown("- Presentation of results at quality reviews")
		
		st.markdown("#### **Skills**")
		st.markdown("- FEA Solver: NASTRAN")
		st.markdown("- FEA Preprocessor: NASTRAN/Hyperworks")
		st.markdown("- Automation of processes through MATLAB scripts")
		st.markdown("- Mentoring contractors and graduates")
		
		st.markdown("#### **Projects**")
		
		# #### BLADE ####
		col1, col2 = st.columns(2)
		with col1:
			st.image(blade_image)
			
		with col2:
			st.markdown("### A340 BLADE")
			st.markdown("- Breakthrough Laminar Aircraft Demonstrator in Europe (BLADE)")
			st.markdown("- ")

		# #### BLADE ####
		col1, col2 = st.columns(2)	

		with col2:
			st.markdown("### A330 NEO")
			st.markdown("- Team lead for A330 NEO activties")
			st.markdown("- Involved in early sensitivity studies of possible revised winglet loads through until certification model GFEM")


	with st.expander("Eirtech Aviation - Design Engineer - November 2016 to June 2018 - Shannon, Ireland"):
		st.markdown("#### **Role Duties**")
		

	with st.expander("Wood PLC - Senior Engineer - June 2018 to August 2022 - Galway, Ireland"):
		col1, col2 = st.columns(2)	
		
		with col1:
			st.markdown("#### **Role Duties**")
			
			st.markdown("- FEA analysis of offshore drilling risers")
			st.markdown("- Preparation of FEA models based on client inputs (e.g. vessel data, water depth, local environmental data, etc)")
			st.markdown("- Static and Dynamic FEA analysis")
			st.markdown("- Generation of operatiional envelopes for use by the Drilling Rig team during drilling operations")
			st.markdown("- Calculation of fatigue lives")
			st.markdown("- Preparation of technical reports detailing results and conclusions")
			
			st.subheader("Skills")
			st.markdown("- FEA Solvers/Preprocessors: Deepriser/Flexcom")
			st.markdown("- VIV (Vortex Induced Vibration) Software: Shear7")
			st.markdown("- Fatigue Life Calculation")
			st.markdown("- Project Managment")
			
		with col2:
			st.markdown("##### Typical Drilling Riser System;")
			st.image(riser_image)
		
		
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











	