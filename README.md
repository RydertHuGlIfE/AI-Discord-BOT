# AI-Discord-BOT
This is an AI discord bot powered by the gemini model.


# Gemini Discord Bot

This Discord bot leverages the Gemini API to provide an interactive chat experience within your Discord server. It offers various commands for conversation, bot management, and developer utilities.

## Features

*   **Chat:** Engage in dynamic conversations with the bot using the `/chat` command. The bot utilizes the Gemini API to generate responses based on your prompts.
*   **Reply:** Continue previous conversations with the bot using the `/reply` command. The bot maintains a conversation history for each user, allowing for context-aware responses.
*   **Refresh:** Clear the bot's context and logs using the `/refresh` command. This command is restricted to the bot's owner.
*   **Ping:** Check the bot's latency with the `/ping` command. This displays the round-trip time in milliseconds.
*   **About:** Learn more about the bot and its developer with the `/about` command.
*   **Shutdown:** Safely shut down the bot using the `/shutdown` command. This command is restricted to the bot's owner.
*   **Show Logs:** View unauthorized command usage logs with the `/show_logs` command. This command is restricted to the bot's owner and displays logs privately (ephemeral).
*   **Show Users:** Display a list of active users and their message counts using the `/show_users` command. This command is restricted to the bot's owner.
*   **Context Clear:** Clear all user conversation contexts with the `/context_clear` command. This command is restricted to the bot's owner.

## Commands

| Command        | Description                                                                    |
|----------------|--------------------------------------------------------------------------------|
| `/chat <prompt>` | Starts a new conversation with the bot.                                       |
| `/reply <prompt>`| Continues the existing conversation with the bot, using the conversation history. |
| `/refresh`       | Clears the bot's context and logs. (Owner Only)                               |
| `/ping`          | Displays the bot's latency.                                                    |
| `/about`         | Provides information about the bot.                                           |
| `/shutdown`      | Shuts down the bot. (Owner Only)                                              |
| `/show_logs`     | Displays unauthorized command usage logs. (Owner Only)                          |
| `/show_users`    | Displays active users and their message counts. (Owner Only)                     |
| `/context_clear`  | Clears all user conversation contexts. (Owner Only)                             |

## Installation

1.  **Clone the Repository:** Clone this repository to your local machine.
2.  **Install Dependencies:** Install the required Python packages using `pip install -r requirements.txt` (you'll need to create a `requirements.txt` file listing the dependencies: `discord.py`, `google-generativeai`).
3.  **Configure API Key:** Replace `"AIzaSyAmdmSD8cLq7OgUUqvxIk1MwBJDwmUKGsI"` in the code with your actual Gemini API key.
4.  **Run the Bot:** Execute the Python script to start the bot.

## Usage

Once the bot is running, you can add it to your Discord server and use the commands listed above.  Remember that slash commands might need to be synced with your server after the bot starts. The code already includes a sync command, but you may need to run it manually if you encounter issues.

## Developer

This bot is developed by `__ryder__2001__`.

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues.

## License

[Specify the license under which the project is distributed]

## Disclaimer

This bot uses the Gemini API. Please review the API's terms of service and usage guidelines.
