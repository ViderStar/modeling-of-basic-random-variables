import numpy as np
import plotly.graph_objects as go

def LabWork5():
    def solve(A, f, num_chains, chain_length):
        n = A.shape[0]
        x = np.zeros(n)
        for j in range(n):
            for _ in range(num_chains):
                weight = 1
                state_prev = j
                x[j] += f[j]
                for _ in range(chain_length):
                    state_new = np.random.choice(n)
                    weight *= n * A[state_prev][state_new]
                    x[j] += weight * f[state_new]
                    state_prev = state_new
        return x / num_chains


    A = np.array([[1.2, -0.4, 0.3],
                  [0.1, 0.7, -0.2],
                  [-0.4, 0.0, 1.4]])
    f = np.array([-3, 1, 4])
    actual_x = np.linalg.solve(A, f)

    A = np.array([[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]]) - A

    num_chains_set = [30, 50, 70, 100]
    chain_length_set = [100, 200, 500, 1000]

    results = {}

    for num_chains in num_chains_set:
        for chain_length in chain_length_set:
            x = solve(A, f, num_chains, chain_length)
            error = np.linalg.norm(x - actual_x)
            results[(num_chains, chain_length)] = error
            print(f'num_chains: {num_chains}')
            print(f'chain_length: {chain_length}')
            print(f'error: {error}\n')

    fig = go.Figure()

    for i, num_chains in enumerate(num_chains_set):
        errors = [results[(num_chains, cl)] for cl in chain_length_set]
        fig.add_trace(go.Scatter(x=chain_length_set, y=errors, mode='lines', name=f'Num Chains: {num_chains}'))

    fig.update_layout(
        title="Error vs Chain Length",
        xaxis_title="Chain Length",
        yaxis_title="Error",
        yaxis_type="log",
        xaxis_type="log",
        legend_title="Number of Chains",
        autosize=False,
        width=800,
        height=500,
        margin=dict(
            l=50,
            r=50,
            b=100,
            t=100,
            pad=4
        ),
        paper_bgcolor="LightSteelBlue",
    )

    fig.show()
