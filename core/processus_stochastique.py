import numpy as np

def simulate_markov_chain(P, initial_state=0, steps=10):
    """
    Simule une chaîne de Markov.
    P : matrice de transition (numpy array)
    initial_state : état de départ (int)
    steps : nombre d'étapes à simuler
    """
    n = P.shape[0]
    trajectory = [initial_state]
    current_state = initial_state

    for _ in range(steps):
        current_state = np.random.choice(n, p=P[current_state])
        trajectory.append(current_state)

    return trajectory

# Test rapide
if __name__ == "__main__":
    P = np.array([[0.1, 0.6, 0.3],
                  [0.4, 0.4, 0.2],
                  [0.3, 0.3, 0.4]])
    traj = simulate_markov_chain(P, initial_state=0, steps=10)
    print("Trajectoire simulée :", traj)
