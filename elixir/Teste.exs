defmodule User do
  defstruct [:name, :id, :role]

  def add_user(new_user, user) do
    if user.role == :admin do
      new_user
    end
    else
      :error

    end
  end
end
