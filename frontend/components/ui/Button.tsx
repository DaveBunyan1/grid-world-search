interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  children: React.ReactNode;
}

export default function Button({
  children,
  className = "",
  ...props
}: ButtonProps) {
  return (
    <button
      {...props}
      className={`
        border px-4 py-2
        hover:bg-slate-800
        cursor-pointer
        disabled:opacity-50
        disabled:cursor-not-allowed
        transition-colors
        ${className}
      `}
    >
      {children}
    </button>
  );
}
