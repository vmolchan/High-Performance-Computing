from cffi import FFI
ffibuilder = FFI()

#########################
### Add API Code Here ###
#########################

ffibuilder.set_source("iterate_api",
                     r"""
                     
                     #include <math.h>

                        double iterate(double *u, int nx, int ny, const double dx, const double dy) {
                            double err = 0.0;
                            double tmp, diff;
                            int i, j;

                            for (j = 1; j < ny - 1; ++j) {
                                for (i = 1; i < nx - 1; ++i) {
                                    tmp = u[i + nx * j];
                                    u[i + nx * j] =
                                        ((u[(i - 1) + nx * j] + u[(i + 1) + nx * j]) * dy * dy +
                                         (u[i + nx * (j - 1)] + u[i + nx * (j + 1)]) * dx * dx) /
                                        (dx * dx + dy * dy) / 2;
                                    diff = u[i + nx * j] - tmp;
                                    err += diff * diff;
                                }
                            }
                            return sqrt(err);
                        }

                     
                     """ 
                     )
ffibuilder.cdef("""double iterate(double *u, int nx, int ny, const double dx, const double dy);""")

#########################
###                   ###
#########################

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
