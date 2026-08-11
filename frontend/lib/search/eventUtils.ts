import { SearchEvent } from "@/types/api";

export function eventToPositionSet(events: SearchEvent[]) {
  return new Set(events.map((event) => `${event.node.row}-${event.node.col}`));
}
