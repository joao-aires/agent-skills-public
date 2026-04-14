#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────
# sync-skills.sh — Manage symlinks from this repo's skills/ into
#                  ~/.agents/skills/ so they are available globally.
#
# Usage:
#   ./sync-skills.sh [sync|status|remove] [skill_name|all]
#
# Examples:
#   ./sync-skills.sh sync                 # sync all skills
#   ./sync-skills.sh sync my_skill        # sync only my_skill
#   ./sync-skills.sh remove all           # remove all skills
# ─────────────────────────────────────────────────────────────────────
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SOURCE_DIR="$REPO_ROOT/skills"
TARGET_DIR="$HOME/.agents/skills"

# Compute a relative path from $2 to $1 (macOS-compatible, no GNU coreutils)
relpath() {
  python3 -c "import os, sys; print(os.path.relpath(sys.argv[1], sys.argv[2]))" "$1" "$2"
}

# Collect skill directory names managed by this repo
repo_skills() {
  local target="${1:-all}"
  if [[ "$target" == "all" ]]; then
    find "$SOURCE_DIR" -mindepth 1 -maxdepth 1 -type d -exec basename {} \; | sort
  else
    if [[ ! -d "$SOURCE_DIR/$target" ]]; then
      echo "Error: Skill '$target' not found in $SOURCE_DIR" >&2
      exit 1
    fi
    echo "$target"
  fi
}

# ── sync (default) ──────────────────────────────────────────────────
do_sync() {
  local target="${1:-all}"
  mkdir -p "$TARGET_DIR"

  local created=0 updated=0 skipped=0

  for skill in $(repo_skills "$target"); do
    local src="$SOURCE_DIR/$skill"
    local dest="$TARGET_DIR/$skill"
    local rel
    rel="$(relpath "$src" "$TARGET_DIR")"

    if [[ -L "$dest" ]]; then
      local current
      current="$(readlink "$dest")"
      if [[ "$current" == "$rel" ]]; then
        echo "  ✓  $skill (already up-to-date)"
        (( skipped++ )) || true
        continue
      fi
      rm "$dest"
      ln -s "$rel" "$dest"
      echo "  ↻  $skill (updated: $current → $rel)"
      (( updated++ )) || true
    elif [[ -e "$dest" ]]; then
      echo "  ⚠  $skill — target exists and is not a symlink, skipping"
      (( skipped++ )) || true
    else
      ln -s "$rel" "$dest"
      echo "  +  $skill → $rel"
      (( created++ )) || true
    fi
  done

  echo ""
  echo "Done: $created created, $updated updated, $skipped skipped."
}

# ── status ──────────────────────────────────────────────────────────
do_status() {
  local target="${1:-all}"
  for skill in $(repo_skills "$target"); do
    local dest="$TARGET_DIR/$skill"
    if [[ -L "$dest" ]]; then
      echo "  ✓  $skill → $(readlink "$dest")"
    elif [[ -e "$dest" ]]; then
      echo "  ⚠  $skill (exists but not a symlink)"
    else
      echo "  ✗  $skill (not linked)"
    fi
  done
}

# ── remove ──────────────────────────────────────────────────────────
do_remove() {
  local target="${1:-all}"
  local removed=0
  for skill in $(repo_skills "$target"); do
    local dest="$TARGET_DIR/$skill"
    if [[ -L "$dest" ]]; then
      rm "$dest"
      echo "  -  $skill"
      (( removed++ )) || true
    fi
  done
  echo ""
  echo "Removed $removed symlink(s)."
}

# ── main ────────────────────────────────────────────────────────────
# If arguments are provided but don't match our subcommands, assume it's a skill name for 'sync'
if [[ $# -ge 1 ]] && [[ "$1" != "sync" ]] && [[ "$1" != "status" ]] && [[ "$1" != "remove" ]]; then
  do_sync "$1"
  exit 0
fi

case "${1:-sync}" in
  sync)   do_sync "${2:-all}"   ;;
  status) do_status "${2:-all}" ;;
  remove) do_remove "${2:-all}" ;;
  *)
    echo "Usage: $0 {sync|status|remove} [skill_name|all]" >&2
    exit 1
    ;;
esac
