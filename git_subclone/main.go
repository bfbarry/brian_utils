package main

import (
	"fmt"
	"os"
	"os/exec"
)

func main() {
	repoURL := "https://github.com/user/repo.git"
	cloneDir := "repo_clone"
	targetFolder := "subdir"

	// Initialize a new repository
	cmds := [][]string{
		{"git", "init", cloneDir},
		{"git", "-C", cloneDir, "remote", "add", "origin", repoURL},
		{"git", "-C", cloneDir, "config", "core.sparseCheckout", "true"},
		{"sh", "-c", fmt.Sprintf("echo %s > %s/.git/info/sparse-checkout", targetFolder, cloneDir)},
		{"git", "-C", cloneDir, "pull", "origin", "main"}, // Change 'main' if necessary
	}

	for _, cmdArgs := range cmds {
		cmd := exec.Command(cmdArgs[0], cmdArgs[1:]...)
		cmd.Stdout = os.Stdout
		cmd.Stderr = os.Stderr
		if err := cmd.Run(); err != nil {
			fmt.Println("Error:", err)
			return
		}
	}

	fmt.Println("Folder cloned successfully:", filepath.Join(cloneDir, targetFolder))
}
