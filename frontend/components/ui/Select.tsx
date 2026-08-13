"use client";

import { useState, useRef, useEffect } from "react";

interface SelectOption {
  value: string;
  label: string;
}

interface SelectProps {
  value: string;
  options: SelectOption[];
  onChange: (value: string) => void;
  placeholder?: string;
  disabled?: boolean;
}

export default function Select({
  value,
  options,
  onChange,
  placeholder = "Select...",
  disabled = false,
}: SelectProps) {
  const [open, setOpen] = useState(false);
  const containerRef = useRef<HTMLDivElement>(null);

  const selectedOption = options.find((option) => option.value === value);

  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (
        containerRef.current &&
        !containerRef.current.contains(event.target as Node)
      ) {
        setOpen(false);
      }
    }

    document.addEventListener("mousedown", handleClickOutside);

    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, []);

  function handleSelect(option: SelectOption) {
    onChange(option.value);
    setOpen(false);
  }

  const longestLabel = options.reduce(
    (longest, option) =>
      option.label.length > longest.length ? option.label : longest,
    "",
  );

  return (
    <div ref={containerRef} className="relative w-fit">
      <button
        type="button"
        disabled={disabled}
        onClick={() => setOpen((previous) => !previous)}
        className="
          flex w-full items-center justify-between
          border border-slate-600
          bg-slate-900
          px-4 py-2
          text-left text-sm text-slate-100
          transition-colors
          hover:bg-slate-800
          focus:outline-none
          focus:ring-2 focus:ring-slate-500
          disabled:cursor-not-allowed
          disabled:opacity-50
        "
      >
        <span className="invisible whitespace-nowrap">{longestLabel}</span>

        <span className="absolute left-4 whitespace-nowrap">
          {selectedOption?.label ?? placeholder}
        </span>

        <span
          className={`ml-4 transition-transform ${open ? "rotate-180" : ""}`}
        >
          ▼
        </span>
      </button>

      {open && (
        <div
          className="
            absolute z-50 mt-1 w-full
            overflow-hidden
            border border-slate-700
            bg-slate-900
            shadow-lg
          "
        >
          {options.map((option) => (
            <button
              key={option.value}
              type="button"
              onClick={() => handleSelect(option)}
              className={`
                block w-full
                px-4 py-2
                text-left text-sm
                transition-colors
                hover:bg-slate-800
                ${
                  option.value === value
                    ? "bg-slate-800 text-slate-100"
                    : "text-slate-300"
                }
              `}
            >
              {option.label}
            </button>
          ))}
        </div>
      )}
    </div>
  );
}
