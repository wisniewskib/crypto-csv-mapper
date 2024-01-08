import curses


def print_menu(stdscr, selected_row_idx, options):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    menu_title = "Select exchange of file you want to convert to DeltaApp format"
    stdscr.addstr(h // 2 - 2, w // 2 - len(menu_title) // 2, menu_title)
    for idx, row in enumerate(options):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(options) // 2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    options = ["Xeggex", "MEXC"]
    current_row = 0

    print_menu(stdscr, current_row, options)

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(options) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.addstr(0, 0, f"You selected '{options[current_row]}' ")
            stdscr.refresh()
            stdscr.getch()
            if current_row == len(options) - 1:
                break

        print_menu(stdscr, current_row, options)


curses.wrapper(main)
