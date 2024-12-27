import numpy as np
import matplotlib.pyplot as plt


def problem_1(N=20, T=4, u0=1):

    N = 20 # Number of time steps
    T = 4 # Final time
    dt = T/N
    u0 = 1 # Initial condition

    # Create arrays t and u of length N + 1^1
    # Set initial condition:    u[0] = u0
    #                           t[0] = 0
    # Compute time step delta t dt = T/N
    # For n = 0, 1, 2, ..., N-1:
    #       t[n+1] = t[n] + dt
    #       u[n+1] = (1 + dt) * u[n]

    t = np.zeros(N + 1)
    u = np.zeros(N + 1)

    u[0] = u0
    # t[0] is already 0 from np.zeroes
    for n in range(N):
        t[n+1] = t[n] + dt
        u[n+1] = (1 + dt) * u[n]

        # Or...
        # for n in range(1, N+1):
        #   t[n] = t[n-1] + dt
        #   u[n] = (1 + dt) * u[n - 1]

    plt.plot(t, u)
    plt.show()


if __name__ == "__main__":
    problem_1()
