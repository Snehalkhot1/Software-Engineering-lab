class Task {
    constructor(title, priority, status = "To Do") {
        this.title = title;
        this.priority = priority;
        this.status = status;
    }
}

class ScrumMethod {
    constructor() {
        this.backlog = [
            new Task("User login page", "High"),
            new Task("Payment gateway", "High"),
            new Task("Send email notification", "Medium"),
            new Task("Admin dashboard", "Low")
        ];
    }

    planSprint(sprintSize = 3) {
        const sprintItems = this.backlog.slice(0, sprintSize);
        return sprintItems.map(task => task.title);
    }

    dailyUpdate() {
        return {
            Completed: "Login page built",
            "In Progress": "Payment gateway integration",
            Blocked: "Waiting for API credentials"
        };
    }
}

class KanbanMethod {
    constructor() {
        this.board = {
            "To Do": ["Create signup form", "Add search feature"],
            "In Progress": ["Fix login bug"],
            Review: ["Update profile page"],
            Done: ["Homepage design"]
        };
    }

    moveTask(taskName, fromColumn, toColumn) {
        if (this.board[fromColumn] && this.board[fromColumn].includes(taskName)) {
            this.board[fromColumn] = this.board[fromColumn].filter(task => task !== taskName);
            if (!this.board[toColumn]) {
                this.board[toColumn] = [];
            }
            this.board[toColumn].push(taskName);
            return `Moved '${taskName}' from ${fromColumn} to ${toColumn}.`;
        }
        return `Task '${taskName}' not found in ${fromColumn}.`;
    }

    showBoard() {
        return this.board;
    }
}

class ExtremeProgrammingMethod {
    constructor() {
        this.userStories = [
            "As a user, I want to log in securely.",
            "As a user, I want to reset my password.",
            "As an admin, I want to manage orders."
        ];
    }

    pairProgrammingCycle(story) {
        return {
            Story: story,
            "Step 1": "Write a failing test",
            "Step 2": "Write minimal code",
            "Step 3": "Refactor and improve quality"
        };
    }

    continuousIntegration() {
        return "Code is tested and integrated after every small change.";
    }
}

function printAgileDemo() {
    const scrum = new ScrumMethod();
    const kanban = new KanbanMethod();
    const xp = new ExtremeProgrammingMethod();

    console.log("=== Scrum Method ===");
    console.log("Sprint backlog:", scrum.planSprint());
    console.log("Daily update:", scrum.dailyUpdate());

    console.log("\n=== Kanban Method ===");
    console.log("Current board:", kanban.showBoard());
    console.log(kanban.moveTask("Fix login bug", "In Progress", "Review"));
    console.log("Updated board:", kanban.showBoard());

    console.log("\n=== Extreme Programming (XP) ===");
    console.log(xp.pairProgrammingCycle(xp.userStories[0]));
    console.log(xp.continuousIntegration());
}

printAgileDemo();