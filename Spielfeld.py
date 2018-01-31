from tkinter import *

global spieler1
spieler1 = 1
global spieler2
spieler2 = 2
global spieler
spieler = 1
Reihe1 = [0, 0, 0]
Reihe2 = [0, 0, 0]
Reihe3 = [0, 0, 0]


def aa():
    global spieler
    Reihe1[1] = spieler
    if spieler == 1:
        spieler = 2
        x1y1.configure(background="yellow")
    else:
        spieler = 1
        x1y1.configure(background="green")

    # if x1y1 == x2y1 & x2y1 == x3y1:
    ######
    # else:
    #   if x1y2 == x2y2 & x2y2 == x3y2:
    ##########
    #  else:
    #     if x1y3 == x2y3 & x2y3 == x3y3:
    ##########
    #    else:
    #       if x1y1 == x1y2 & x1y2 == x1y3:
    ###########
    #      else:
    #         if x2y1 == x2y2 & x2y2 == x2y3:
    #######
    #        else:
    #           if x3y1 == x3y2 & x3y2 == x3y3:
    ########
    #          else:
    #             if x1y1 == x2y2 & x2y2 == x3y3:
    #######
    #            else:
    #               if x3y1 == x2y2 & x2y2 == x1y3:
    ##########
    #              else:
    #                 if (x1y1 != 0) & (x1y2 != 0) & (x1y3 != 0) & (x2y1 != 0) & (x2y2 != 0) & (
    #                        x2y3 != 0) & (x3y1 != 0) & (x3y2 != 0) & (x3y3 != 0):
    ############


def ba():
    global spieler
    Reihe1[2] = spieler
    if spieler == 1:
        spieler = 2
        x2y1.configure(background="yellow")
    else:
        spieler = 1
        x2y1.configure(background="green")

        #   if x1y1 == x2y1 & x2y1 == x3y1:
        ######
        #  else:
        if x1y2 == x2y2 & x2y2 == x3y2:
            pass
    ##########


#     else:
#        if x1y3 == x2y3 & x2y3 == x3y3:
##########
#       else:
#          if x1y1 == x1y2 & x1y2 == x1y3:
###########
#         else:
#            if x2y1 == x2y2 & x2y2 == x2y3:
#           #######
#          else:
#             if x3y1 == x3y2 & x3y2 == x3y3:
########
#            else:
#               if x1y1 == x2y2 & x2y2 == x3y3:
#######
#              else:
#                 if x3y1 == x2y2 & x2y2 == x1y3:
##########
#                else:
#                   if (x1y1 != 0) & (x1y2 != 0) & (x1y3 != 0) & (x2y1 != 0) & (x2y2 != 0) & (
#                          x2y3 != 0) & (x3y1 != 0) & (x3y2 != 0) & (x3y3 != 0):
############


def ca():
    global spieler
    Reihe1[3] = spieler
    if spieler == 1:
        spieler = 2
        x3y1.configure(background="yellow")
    else:
        spieler = 1
        x3y1.configure(background="green")

    # if x1y1 == x2y1 & x2y1 == x3y1:
    ######
    # else:
    #   if x1y2 == x2y2 & x2y2 == x3y2:
    ##########
    #  else:
    #     if x1y3 == x2y3 & x2y3 == x3y3:
    ##########
    #    else:
    #       if x1y1 == x1y2 & x1y2 == x1y3:
    ###########
    #      else:
    #         if x2y1 == x2y2 & x2y2 == x2y3:
    #######
    #        else:
    #           if x3y1 == x3y2 & x3y2 == x3y3:
    ########
    #          else:
    #             if x1y1 == x2y2 & x2y2 == x3y3:
    #######
    #            else:
    #               if x3y1 == x2y2 & x2y2 == x1y3:
    ##########
    #              else:
    #                 if (x1y1 != 0) & (x1y2 != 0) & (x1y3 != 0) & (x2y1 != 0) & (x2y2 != 0) & (
    #                        x2y3 != 0) & (x3y1 != 0) & (x3y2 != 0) & (x3y3 != 0):
    ############


def da():
    global spieler
    Reihe2[1] = spieler
    if spieler == 1:
        spieler = 2
        x1y2.configure(background="yellow")
    else:
        spieler = 1
        x1y2.configure(background="green")

    # if x1y1 == x2y1 & x2y1 == x3y1:
    ######
    # else:
    #   if x1y2 == x2y2 & x2y2 == x3y2:
    ##########
    #  else:
    #     if x1y3 == x2y3 & x2y3 == x3y3:
    ##########
    #    else:
    #       if x1y1 == x1y2 & x1y2 == x1y3:
    ###########
    #      else:
    #         if x2y1 == x2y2 & x2y2 == x2y3:
    #######
    #        else:
    #           if x3y1 == x3y2 & x3y2 == x3y3:
    ########
    #          else:
    #             if x1y1 == x2y2 & x2y2 == x3y3:
    #######
    #            else:
    #               if x3y1 == x2y2 & x2y2 == x1y3:
    ##########
    #              else:
    #                 if (x1y1 != 0) & (x1y2 != 0) & (x1y3 != 0) & (x2y1 != 0) & (x2y2 != 0) & (
    #                        x2y3 != 0) & (x3y1 != 0) & (x3y2 != 0) & (x3y3 != 0):
    ############


def ea():
    global spieler
    Reihe2[2] = spieler
    if spieler == 1:
        spieler = 2
        x2y2.configure(background="yellow")
    else:
        spieler = 1
        x2y2.configure(background="green")

    # if x1y1 == x2y1 & x2y1 == x3y1:
    ######
    # else:
    #   if x1y2 == x2y2 & x2y2 == x3y2:
    ##########
    #  else:
    #     if x1y3 == x2y3 & x2y3 == x3y3:
    ##########
    #    else:
    #       if x1y1 == x1y2 & x1y2 == x1y3:
    ###########
    #      else:
    #         if x2y1 == x2y2 & x2y2 == x2y3:
    #######
    #        else:
    #           if x3y1 == x3y2 & x3y2 == x3y3:
    ########
    #          else:
    #             if x1y1 == x2y2 & x2y2 == x3y3:
    #######
    #            else:
    #               if x3y1 == x2y2 & x2y2 == x1y3:
    ##########
    #              else:
    #                 if (x1y1 != 0) & (x1y2 != 0) & (x1y3 != 0) & (x2y1 != 0) & (x2y2 != 0) & (
    #                        x2y3 != 0) & (x3y1 != 0) & (x3y2 != 0) & (x3y3 != 0):
    ############


def fa():
    global spieler
    Reihe2[3] = spieler
    if spieler == 1:
        spieler = 2
        x3y2.configure(background="yellow")
    else:
        spieler = 1
        x3y2.configure(background="green")

    #   if x1y1 == x2y1 & x2y1 == x3y1:
    ######
    #  else:
    #     if x1y2 == x2y2 & x2y2 == x3y2:
    ##########
    #    else:
    #       if x1y3 == x2y3 & x2y3 == x3y3:
    ##########
    #      else:
    #         if x1y1 == x1y2 & x1y2 == x1y3:
    ###########
    #        else:
    #           if x2y1 == x2y2 & x2y2 == x2y3:
    #######
    #          else:
    #             if x3y1 == x3y2 & x3y2 == x3y3:
    ########
    #            else:
    #               if x1y1 == x2y2 & x2y2 == x3y3:
    #######
    #              else:
    #                 if x3y1 == x2y2 & x2y2 == x1y3:
    ##########
    #                else:
    #                   if (x1y1 != 0) & (x1y2 != 0) & (x1y3 != 0) & (x2y1 != 0) & (x2y2 != 0) & (
    #                         x2y3 != 0) & (x3y1 != 0) & (x3y2 != 0) & (x3y3 != 0):
    #              ############


def ga():
    global spieler
    Reihe3[1] = spieler
    if spieler == 1:
        spieler = 2
        x1y3.configure(background="yellow")
    else:
        spieler = 1
        x1y3.configure(background="green")

    # if x1y1 == x2y1 & x2y1 == x3y1:
    ######
    # else:
    #   if x1y2 == x2y2 & x2y2 == x3y2:
    ##########
    #  else:
    #     if x1y3 == x2y3 & x2y3 == x3y3:
    ##########
    #    else:
    #       if x1y1 == x1y2 & x1y2 == x1y3:
    ###########
    #      else:
    #         if x2y1 == x2y2 & x2y2 == x2y3:
    #######
    #        else:
    #           if x3y1 == x3y2 & x3y2 == x3y3:
    ########
    #          else:
    #             if x1y1 == x2y2 & x2y2 == x3y3:
    #######
    #            else:
    #               if x3y1 == x2y2 & x2y2 == x1y3:
    ##########
    #              else:
    #                 if (x1y1 != 0) & (x1y2 != 0) & (x1y3 != 0) & (x2y1 != 0) & (x2y2 != 0) & (
    #                        x2y3 != 0) & (x3y1 != 0) & (x3y2 != 0) & (x3y3 != 0):
    ############


def ha():
    global spieler
    Reihe3[2] = spieler
    if spieler == 1:
        spieler = 2
        x2y3.configure(background="yellow")
    else:
        spieler = 1
        x2y3.configure(background="green")


#   if x1y1 == x2y1 & x2y1 == x3y1:
######
#  else:
#     if x1y2 == x2y2 & x2y2 == x3y2:
##########
#    else:
#       if x1y3 == x2y3 & x2y3 == x3y3:
##########
#      else:
#         if x1y1 == x1y2 & x1y2 == x1y3:
###########
#        else:
#           if x2y1 == x2y2 & x2y2 == x2y3:
#######
#          else:
#             if x3y1 == x3y2 & x3y2 == x3y3:
########
#            else:
#               if x1y1 == x2y2 & x2y2 == x3y3:
#######
#              else:
#                 if x3y1 == x2y2 & x2y2 == x1y3:
##########
#                else:
#                   if (x1y1 != 0) & (x1y2 != 0) & (x1y3 != 0) & (x2y1 != 0) & (x2y2 != 0) & (
#                          x2y3 != 0) & (x3y1 != 0) & (x3y2 != 0) & (x3y3 != 0):
############


def ia():
    global spieler
    Reihe3[2] = spieler
    if spieler == 1:
        spieler = 2
        x3y3.configure(background="yellow")
    else:
        spieler = 1
        x3y3.configure(background="green")


#  if x1y1 == x2y1 & x2y1 == x3y1:
######
# else:
#    if x1y2 == x2y2 & x2y2 == x3y2:
##########
#   else:
#      if x1y3 == x2y3 & x2y3 == x3y3:
##########
#     else:
#        if x1y1 == x1y2 & x1y2 == x1y3:
###########
#       else:
#          if x2y1 == x2y2 & x2y2 == x2y3:
#######
#         else:
#            if x3y1 == x3y2 & x3y2 == x3y3:
########
#           else:
#              if x1y1 == x2y2 & x2y2 == x3y3:
#######
#             else:
#                if x3y1 == x2y2 & x2y2 == x1y3:
##########
#               else:
#                  if (x1y1 != 0) & (x1y2 != 0) & (x1y3 != 0) & (x2y1 != 0) & (x2y2 != 0) & (
#                         x2y3 != 0) & (x3y1 != 0) & (x3y2 != 0) & (x3y3 != 0):
############


Feld = Tk()
Feld.title("Spielfeld")
x1y1 = Button(Feld, command=aa)
x2y1 = Button(Feld, command=ba)
x3y1 = Button(Feld, command=ca)
x1y2 = Button(Feld, command=da)
x2y2 = Button(Feld, command=ea)
x3y2 = Button(Feld, command=fa)
x1y3 = Button(Feld, command=ga)
x2y3 = Button(Feld, command=ha)
x3y3 = Button(Feld, command=ia)
x1y1.pack(padx=5, pady=10, side=LEFT)
x1y2.pack(padx=5, pady=10, side=LEFT)
x1y3.pack(padx=5, pady=10, side=LEFT)
x2y1.pack(padx=5, pady=10, side=LEFT)
x2y2.pack(padx=5, pady=10, side=LEFT)
x2y3.pack(padx=5, pady=10, side=LEFT)
x3y1.pack(padx=5, pady=10, side=LEFT)
x3y2.pack(padx=5, pady=10, side=LEFT)
x3y3.pack(padx=5, pady=10, side=LEFT)
Feld.mainloop()
