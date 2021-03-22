from libweek8 import gen_samples, gen_prototype

def main(n_dots, lrn_dists, plot_resolution):
    p_type = gen_prototype(n_dots) 
    gen_samples()



from itertools import product

class Grid():

    def __init__(resolution):
        self.w = resolution[0]
        self.h = resolution[1]
        self.tiles = generatere tiles    
    
    def update_resolution(resolution):
        self.w = resolution[0]
        self.h = resolution[1]

    def get_centers(self, shape):
        offset = 10
        w_centers = np.linspace(offset, self.w - offset, shape[0])
        h_centers = np.linspace(offset, self.h - offset, shape[1])
        # an array of (width,height) tuples
        return np.array(list(product(w_centers,h_centers)))

    def draw(self, matrix, shape, screen):
        centers = self.get_centers(shape)
        for c_indx, tile in enumerate(self.tiles):
            tile.draw_leptons(centers[c_indx], matrix[c_indx], shape, screen, self.w, self.h)

    def normalize(self, matrix):
        return None
        
        
def draw_leptons(centers, plot_vec, shape, screen, w, h):
    # takes coordinates
    circle(plot_vec[0]*w/(shape[0]*2)+centers[0], plot_vec[1]*h/(shape[1]*2)+centers[1], RED, w, h, screen)
    circle(plot_vec[2]*w/(shape[0]*2)+centers[0], plot_vec[3]*h/(shape[1]*2)+centers[1], BLUE, w, h, screen)    
    circle(plot_vec[4]*w/(shape[0]*2)+centers[0], plot_vec[5]*h/(shape[1]*2)+centers[1], GREEN, w, h, screen)
    # Make relative location scalable with size in such a way, that we can adjust the size of each tile realtive to the overall size of the plot