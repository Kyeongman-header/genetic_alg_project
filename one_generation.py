from consts import *
import time
import random


def gene_maker(nucleobase,length_of_gene):
    gene=[]
    for i in range(length_of_gene):
        gene.append(random.choice(nucleobase))
    return gene

def move(ball,width, height,x_speed,y_speed,rec_start_x,rec_start_y,rec_end_x,rec_end_y,canvas):
    ball_coor=canvas.coords(ball)
    start_x=ball_coor[0]
    start_y=ball_coor[1]
    end_x=ball_coor[2]
    end_y=ball_coor[3]
    touch=False
    inside_rec=False
    if start_x<=0 or end_x>=width:
    # or (start_x>=rec_start_x and start_y>=rec_start_y):
        x_speed=-x_speed
        touch=True
    if start_y<=0 or end_y>=height: 
    #or (end_x<=rec_end_x and end_y<=rec_end_y):
        y_speed=-y_speed
        touch=True
    
    if end_x>=rec_start_x and end_y >= rec_start_y and start_x<=rec_end_x and start_y <= rec_end_y:
        canvas.itemconfigure(ball,fill="red")
        inside_rec=True
    else:
        canvas.itemconfigure(ball,fill="yellow")
        inside_rec=False

    canvas.move(ball,x_speed,y_speed)
    return x_speed,y_speed,touch,inside_rec

def one_generation(generation,canvas,whole_individuals,is_Test=False,best_gene=[]):
    

    rec_start_x=width//2-50
    rec_start_y=height//2-50
    rec_end_x=width//2+50
    rec_end_y=height//2+50


    results=[]

    for num_of_individual in range(whole_individuals):
        label = tk.Label(window, text=str(generation+1) + " 번째 세대, 개체 " + str(num_of_individual+1) + "번",compound="top")
        if is_Test:
            label = tk.Label(window, text=str(generation+num_of_individual+1) + " 번째 세대의 best.",compound="top")
        label.place(x=width//2-60, y=15)
        score_label=tk.Label(window, text="",compound="top")
        score_label.place(x=15, y=height-15)
        rectangle = canvas.create_rectangle(rec_start_x,rec_start_y,rec_end_x,rec_end_y, fill='blue')

        ball=canvas.create_oval(width//2-20,height//2-20,width//2+20,height//2+20,fill="red",tags=str(num_of_individual))
        if len(best_gene)!=0:
            gene=best_gene[num_of_individual]
        else:
            gene=gene_maker(nucleobase,gene_length)
        # 5개의 핵염기로 이루어진 염기 서열.
        # x_speed = -5
        # y_speed = 5
        score=0
        # print(gene)


        for count in range(Time_Limit):
            x_speed,y_speed,touch,inside_rec=move(ball,width,height,gene[count%len(gene)][0],gene[count%len(gene)][1],rec_start_x,rec_start_y,rec_end_x,rec_end_y,canvas)
            score_label.configure(text="time survive : " + str(count) + " not inside time : " + str(count-score))
            window.update()
            if is_Test:
                time.sleep(0.01)
            else:
                time.sleep(0.01)
            # print(canvas.coords(ball))
            # input()
            if touch:
                break # 탈락.
                # gene=[[val * -1 for val in nuc] for nuc in gene]
                # print(gene)
            if inside_rec:
                score+=1

        print("time survive : " + str(count))
        print("not inside rectangle time : " + str(count-score))
        results.append({'gene' : gene,'time_survive' : count,'score' : score})
        canvas.delete("all")
        score_label.configure(text="")
    return results

