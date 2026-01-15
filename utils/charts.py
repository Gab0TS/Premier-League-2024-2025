from matplotlib import pyplot as plt

def generate_bar_chart(labels, values, title):
    fig, ax = plt.subplots()
    bars = ax.bar(labels, values)
    for bar in bars:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            str(int(bar.get_height())),
            ha='center',
            va='bottom'
        )

    ax.set_title(title)
    plt.xticks(rotation=12, ha='right')
    plt.show()

def generate_pie_chart(labels, values, title):
    total = sum(values)
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels,
           autopct=lambda p: f'{int(round(p * total / 100))}')
    ax.set_title(title)
    ax.axis('equal')
    plt.show()