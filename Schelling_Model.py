import numpy as np
import random
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib
import os
import glob

class Schelling_Model:
    
    def __init__(self,city_size, population_ratio, first_satisfaction_threshold, 
        second_satisfaction_threshold, first_rate):

        self.city_size = city_size
        self.population_ratio = population_ratio
        self.first_satisfaction_threshold = first_satisfaction_threshold
        self.second_satisfaction_threshold = second_satisfaction_threshold
        self.first_rate = first_rate

        # Ratio of X and O (-1, 1) Xs and Os (-2,2) planning to occupy (3) and empty houses (0)
        p =[((population_ratio/2)*first_rate), ((population_ratio/2)*first_rate), ((population_ratio/2)*(1-first_rate)), ((population_ratio/2)*(1-first_rate)), (1-population_ratio)]
        grid_size = int(np.sqrt(self.city_size))**2
        self.city = np.random.choice([-1, 1, -2, 2, 0], size=grid_size, p=p)
        self.city = np.reshape(self.city, (int(np.sqrt(grid_size)), int(np.sqrt(grid_size))))


    # Return a list of neighbor agents' type (-2, -1, 0, 1, 2); cspace is always 1; o_row, o_col are using for prevent counting the agent itself.
    def get_neighbor_of_eight(self, row, col, c_space, o_row, o_col):
        neighborhood = []

        if (row-c_space)>=0 and (col-c_space)>=0 and not((row-c_space)==o_row and (col-c_space)==o_col):
            neighborhood.append(self.city[row-c_space, col-c_space])
        if (col-c_space)>=0 and not((row)==o_row and (col-c_space)==o_col):
            neighborhood.append(self.city[row, col-c_space])
        if (row+c_space)<=49 and (col-c_space)>=0 and not((row+c_space)==o_row and (col-c_space)==o_col):
            neighborhood.append(self.city[row+c_space, col-c_space])

        if (row-c_space)>=0 and (col+c_space)<=49 and not((row-c_space)==o_row and (col+c_space)==o_col):
            neighborhood.append(self.city[row-c_space, col+c_space])
        if (col+c_space)<=49 and not((row)==o_row and (col+c_space)==o_col):
            neighborhood.append(self.city[row, col+c_space])
        if (row+c_space)<=49 and (col+c_space)<=49 and not((row+c_space)==o_row and (col+c_space)==o_col):
            neighborhood.append(self.city[row+c_space, col+c_space])
            
        if (row-c_space)>=0 and not((row-c_space)==o_row and (col)==o_col):
            neighborhood.append(self.city[row-c_space, col])
        if (row+c_space)<=49 and not((row+c_space)==o_row and (col)==o_col):
            neighborhood.append(self.city[row+c_space, col])
        return neighborhood

    #Return the tuple that contains row and col that the first satisfied empty space it find. agent (-2, -1, 0, 1, 2)
    def find_closest_empty_house(self, row, col, agent):
        # print("trying to find a satisfy house")
        for cspace in range(1,49):
            min_row = row - cspace
            max_row = row + cspace
            min_col = col - cspace
            max_col = col + cspace

            #top left
            if min_row >=0 and min_col >=0:
                if self.city[row-cspace, col-cspace] == 0:
                    if self.is_satisfaction(row-cspace, col-cspace, agent, row , col):
                        return (row-cspace, col-cspace)
            
            #top right
            if max_row <=49 and min_col >=0:
                if self.city[row+cspace, col-cspace] == 0:
                    if self.is_satisfaction(row+cspace, col-cspace, agent, row , col):
                        return (row+cspace, col-cspace)

            #bottom left
            if min_row >=0 and max_col <=49:
                if self.city[row-cspace, col+cspace] == 0:
                    if self.is_satisfaction(row-cspace, col+cspace, agent, row , col):
                        return (row-cspace, col+cspace)

            #bottom right
            if max_row <=49 and max_col <=49:
                if self.city[row+cspace, col+cspace] == 0:
                    if self.is_satisfaction(row+cspace, col+cspace, agent, row , col):
                        return (row+cspace, col+cspace)           

            #left and right
            for ncol in range(col-(cspace -1), col +(cspace-1)):
                if ncol >=0 and ncol <=49:
                    if min_row >=0:
                        if self.city[min_row, ncol] == 0:
                            if self.is_satisfaction(min_row, ncol, agent, row , col):
                                return (min_row, ncol)
                    if max_row <=49:
                        if self.city[max_row, ncol] == 0:
                            if self.is_satisfaction(max_row, ncol, agent, row , col):
                                return (max_row, ncol)
            #top and down
            for nrow in range(row -(cspace -1), row+(cspace -1)):
                if nrow >=0 and nrow <=49:
                    if min_col >=0:
                        if self.city[nrow, min_col] == 0:
                            if self.is_satisfaction(nrow, min_col, agent, row , col):
                                return (nrow, min_col)
                    if max_col <=49:
                        if self.city[nrow, max_col] == 0:
                            if self.is_satisfaction(nrow, max_col, agent, row , col):
                                return (nrow, max_col)

        return None
    
    #Return the number of simliar agent in a list
    def check_similar(self,a_list, list_size, value):
        count = 0
        for i in range(list_size):
            if value == 1 or value == 2:
                if (a_list[i] ==  1) or (a_list[i]== 2):
                    count = count + 1
            if value == -1 or value == -2:
                if (a_list[i] == -1) or (a_list[i]== -2):
                    count = count + 1            
        return count
    
    #Return a boolean if agent will be satisfied with the selected space.  o_row, o_col are using by get_neighbor_of_eight for prevent counting the agent itself.
    def is_satisfaction(self, row, col, agent, o_row, o_col):
        is_satisfaction = False
        neighborhood = self.get_neighbor_of_eight(row, col, 1, o_row, o_col)
        # print("neighborhood: ",neighborhood)
        neighborhood_size = np.size(neighborhood)
        # print("neighbor size: ",neighborhood_size)
        n_similar = self.check_similar(neighborhood, neighborhood_size, agent)
        # print("n_similar: ", n_similar)

        if agent == 2 or agent == -2:
            is_satisfaction = (n_similar >= self.second_satisfaction_threshold)
        else:
            is_satisfaction = (n_similar >= self.first_satisfaction_threshold)

        return is_satisfaction


    #The main running program.
    def iteration(self):
        # print("iteration start")
        empty_list = []
        x_list = []
        xs_list = []
        o_list = []
        os_list = []
        # count = 0
        for(row, col), value in np.ndenumerate(self.city):
            # print("cell count:", count)
            agent = self.city[row, col]
            if agent != 0 and agent !=3:

                is_unsatisfaction = not self.is_satisfaction(row, col, agent, row, col)
                # print("unsatisfaction: ", is_unsatisfaction)

                if is_unsatisfaction:
                    house_to_go = self.find_closest_empty_house(row, col, agent)
                    # if house_to_go is None:
                        # print("None result")
                    if house_to_go is not None:
                        # print("place to go:", house_to_go)
                        if agent == -1:
                            x_list.append(house_to_go)
                            empty_list.append((row,col))
                        elif agent == -2:
                            xs_list.append(house_to_go)
                            empty_list.append((row,col))
                        elif agent == 2:
                            os_list.append(house_to_go)
                            empty_list.append((row,col))                           
                        elif agent == 1:
                            o_list.append(house_to_go)
                            empty_list.append((row,col))
                        empty_list.append((row,col))
                        self.city[house_to_go] = 3

            # count = count + 1            
        for location in empty_list:
            self.city[location]= 0
        for locationx in x_list:
            self.city[locationx]= -1
        for locationo in o_list:
            self.city[locationo]= 1
        for locationxs in xs_list:
            self.city[locationxs]= -2
        for locationos in os_list:
            self.city[locationos]= 2
        # print("going_to_occupy list:", going_to_occupy)



#Streamlit App Front-end

st.title("Schelling's Model of Segregation")

p_ratio = st.sidebar.slider("Population Ratio", 0., 1., .6)
f_satisfaction_threshold = st.sidebar.slider("First Satisfaction Threshold", 0, 8, 3)
s_satisfaction_threshold = st.sidebar.slider("Second Satisfaction Threshold", 0, 8, 5)
f_rate = st.sidebar.slider("Percentage of People for First Satisfaction Threshold",0., 1., 1.)
n_iterations = st.sidebar.number_input("Number of Iterations", 2)
# pause_button = st.sidebar.button('Pause for Screenshoot (15 second)')
# continue_button = st.sidebar.button('Continue')


schelling = Schelling_Model(2500, p_ratio, f_satisfaction_threshold, 
        s_satisfaction_threshold, f_rate)

#Plot the graphs at initial stage
plt.style.use("ggplot")
plt.figure(figsize=(8, 8))
plt.set_cmap('bwr')
plt.axis('off')
plt.pcolor(schelling.city, vmin=-2, vmax=2, edgecolors='w', linewidths=1)
city_plot = st.pyplot(plt)
step_number = st.empty()
progress_bar = st.progress(0)

if st.sidebar.button('Run Simulation'):

    files = glob.glob('src/*.png', recursive=True)

    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))
        
        plt.savefig('src/iteration0.png')
    for i in range(n_iterations):
        # print("iteration", i+1)
        schelling.iteration()
        # print("iteration end")
        plt.figure(figsize=(8, 8))
        plt.set_cmap('bwr')
        plt.axis('off')
        plt.pcolor(schelling.city, vmin=-2, vmax=2, edgecolors='w', linewidths=1)
        city_plot.pyplot(plt)
        savefile = 'src/iteration' + str(i+1) + '.png' 
        plt.savefig(savefile)
        plt.close("all")
        step_number.text('Iteration' + str(i+1))
        progress_bar.progress((i+1.)/n_iterations)