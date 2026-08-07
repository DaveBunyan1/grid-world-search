import { EditorTool } from "@/types/editor";

interface ToolSelectorProps {
  tool: EditorTool;

  onToolChange(tool: EditorTool): void;
}

export default function ToolSelector({
  tool,
  onToolChange,
}: ToolSelectorProps) {
  return (
    <div className="flex gap-2">
      <button onClick={() => onToolChange("wall")}>Wall</button>

      <button onClick={() => onToolChange("start")}>Start</button>

      <button onClick={() => onToolChange("goal")}>Goal</button>

      <span>Current: {tool}</span>
    </div>
  );
}
