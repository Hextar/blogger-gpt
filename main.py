from utils.agents import get_initial_prompt, show_menu
from utils.io import save_string_to_txt
from utils.langchain import query_gpt_for_blog
from utils.print import (
    print_full_line,
    print_word_count
)


def main():
    print_full_line()

    # Let the user choose an agent to use
    agent = show_menu()

    print(f"💬 Starting chat with agent: \033[1m{agent}\033[0m.\n")

    while True:
        blog_post_title = input(f"📕 Blog post title: ")
        print()

        blog_post_keywords = input(f"🔑 Blog post comma separated keywords: ")
        print()

        # Making sure that the user has entered a valid blog post title
        if not (blog_post_title):
            print(f"🔧 Please enter a valid title.\n")
            continue # skip to the next loop

        initial_prompt = get_initial_prompt(agent)

        response = query_gpt_for_blog(initial_prompt, blog_post_title, blog_post_keywords)

        print_word_count(response)

        save_string_to_txt(response, blog_post_title)

        print_full_line()

        exit()


if __name__ == "__main__":
    main()
