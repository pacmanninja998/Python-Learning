import random
import tkinter as tk

# Global variables
rounds = 0
current_round = 0
player_score = 0
computer_score = 0
rounds_to_win = 0

def round_choice(b):
    global rounds, current_round, player_score, computer_score, rounds_to_win
    menu_window.destroy()
    rounds = b
    player_score = 0
    computer_score = 0
    rounds_to_win = (rounds // 2) + 1
    current_round = 0
    game_screen()

def game_over_button():
    game_window.destroy()
    menu_screen()

def logic(player_hand):
    global current_round, player_score, computer_score
    if current_round < rounds:
        computer_hand = random.choice(["Rock", "Paper", "Scissors"])
        current_round += 1
        
        if player_hand == computer_hand:
            round_winner.config(text= "Tie!")
        else:
            winning_combinations = {
                "Rock": "Scissors",
                "Paper": "Rock", 
                "Scissors": "Paper"
            }
            if winning_combinations[player_hand] == computer_hand:
                player_score += 1
                round_winner.config(text= "<---")
            else:
                computer_score += 1
                round_winner.config(text= "--->")

        player_hand_.config(text=player_hand)
        computer_hand_.config(text=computer_hand)
        score.config(text=f"{player_score} : {computer_score}")
        current_round_label.config(text=f"{current_round} / {rounds}")

        if player_score >= rounds_to_win:
            game_over("Player Won")
        elif computer_score >= rounds_to_win:
            game_over("Computer Won")
        elif current_round == rounds:
            if player_score > computer_score:
                game_over("Player Won")
            elif computer_score > player_score:
                game_over("Computer Won")
            else:
                game_over("Tie")

def menu_screen():
    global menu_window
    menu_window = tk.Tk()
    menu_window.title("Rock Paper Scissors")
    label = tk.Label(menu_window, text="Choose Rounds")
    button3 = tk.Button(menu_window, text="3", command=lambda: round_choice(3), width=10)
    button5 = tk.Button(menu_window, text="5", command=lambda: round_choice(5), width=10)
    button7 = tk.Button(menu_window, text="7", command=lambda: round_choice(7), width=10)
    button9 = tk.Button(menu_window, text="9", command=lambda: round_choice(9), width=10)
    label.grid(row=0, column=0, columnspan=2)
    button3.grid(row=1, column=0)
    button5.grid(row=1, column=1)
    button7.grid(row=2, column=0)
    button9.grid(row=2, column=1)
    menu_window.mainloop()

def game_screen():
    global game_window, label, rock, paper, scissors, player_hand_, computer_hand_
    global round_winner, score, current_round_label, restart
    
    game_window = tk.Tk()
    game_window.title("Rock Paper Scissors")
    
    label = tk.Label(game_window, text="Choose Hand")
    rock = tk.Button(game_window, text="Rock", command=lambda: logic("Rock"), width=12)
    paper = tk.Button(game_window, text="Paper", command=lambda: logic("Paper"), width=12)
    scissors = tk.Button(game_window, text="Scissors", command=lambda: logic("Scissors"), width=12)
    player_label = tk.Label(game_window, text="Player Hand: ")
    round_winner = tk.Label(game_window, text="")
    computer_label = tk.Label(game_window, text="Computer Hand: ")
    score = tk.Label(game_window, text="0 : 0")
    current_round_label = tk.Label(game_window, text=f"0 / {rounds}")
    restart = tk.Button(game_window, text="Game Over", command=game_over_button, width=36)
    player_hand_ = tk.Label(game_window, text="")
    computer_hand_ = tk.Label(game_window, text="")

    label.grid(row=0, column=0, columnspan=3)
    rock.grid(row=1, column=0)
    paper.grid(row=1, column=1)
    scissors.grid(row=1, column=2)
    player_label.grid(row=2, column=0)
    round_winner.grid(row=2, column=1)
    computer_label.grid(row=2, column=2)
    player_hand_.grid(row=3, column=0)
    computer_hand_.grid(row=3, column=2)
    score.grid(row=4, column=1)
    current_round_label.grid(row=5, column=1)
    
    game_window.mainloop()

def game_over(winner):
    round_winner.config(text=winner)
    label.destroy()
    rock.destroy()
    paper.destroy()
    scissors.destroy()
    restart.grid(row=1, column=0, columnspan=3)

menu_screen()