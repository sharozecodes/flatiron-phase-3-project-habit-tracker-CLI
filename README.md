# Habit Tracker CLI Application

## Description

Habit Tracker is a command-line application designed for Flatiron School's third phase project. The app helps users manage and track their habits over time. It leverages a database with two main tables - users and habits, to allow users to monitor their progress and maintain consistency in their daily routines.

## Installation Instructions

### Prerequisites

- Ensure you have `pipenv` installed. If not, you can install it using `pip install pipenv`.

### Steps:

1. Clone the project repository.
2. Navigate to the project directory in your terminal.
3. Set up the virtual environment:

   ```bash
   pipenv install
   pipenv shell
   ```

4. Install the specific version of `sqlalchemy` as the models are designed using it:

   ```bash
   pipenv install sqlalchemy==1.4.41
   ```

5. Install `alembic` for database migrations:

   ```bash
   pip install alembic
   ```

6. Run the database migrations:

   ```bash
   alembic upgrade head
   ```

7. To include demo data in your database, execute the following:
   ```bash
   python seed.py
   ```

## Usage

1. Start the application by running:
   ```bash
   python cli.py
   ```
2. Follow the on-screen prompts to interact with your habits.
3. Habits are time-based. To check-in a habit, you would normally need to wait for the real-time interval to elapse.

### Testing

To save time and test habit check-ins without waiting for real-time intervals, you can use the testing file:

```bash
python habit_test.py
```

This will allow you to simulate checking in any habit ahead of time.

## Contributor's Guide

Contributions are always welcome! Please ensure you:

1. Fork the repository and create your branch from the `main` branch.
2. If you've added code that should be tested, add tests.
3. Ensure the test suite passes.
4. Make sure your code lints (following PEP 8 standards).
5. Issue that pull request!

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Thank you for considering contributing to the Habit Tracker CLI Application and for recognizing its roots in the Flatiron School curriculum!
